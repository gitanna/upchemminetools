#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import csv
import time
from collections import defaultdict, OrderedDict
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.forms import ModelForm
from django.contrib import messages
from django.utils.http import urlquote
#AAfrom guest.decorators import guest_allowed, login_required
from compounddb.models import Compound
from tools.runapp import *
from models import *
from sdftools.moleculeformats import batch_sdf_to_smiles
from simplejson import dumps

#AA@guest_allowed
def launch_job(request, category=None):
    print '\n in launch_job'
    if request.is_ajax():

        # for ajax requests, return HTML form for each app

        currentApp = request.GET['currentApp']
        try:
            application = Application.objects.get(id=currentApp)
            AppFormSet = getAppForm(application.id, request.user)
            form = AppFormSet()
            form = str(form)
            response = dict(form=form, desc=application.description)
        except:
            response = dict(form='ERROR')
        return HttpResponse(dumps(response), 'text/json')
    if request.method == 'POST':
        appForm = getAppForm(request.POST['application'], request.user)
        form = appForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                appid = int(form.cleaned_data['application'])
                application = Application.objects.get(id=str(appid))
            except Application.DoesNotExist:
                messages.error(request, 'Application does not exist')
                return redirect(launch_job, category=category)
        else:
            messages.error(request, str(form.errors))
            return redirect(launch_job, category=category)
        commandOptions, optionsList = parseToolForm(form)

        # setup input

        if application.input_type == 'chemical/x-mdl-sdfile':
            input = 'chemical/x-mdl-sdfile'
        elif application.input_type == 'upload':
            input = request.FILES['File Upload'].read()
            if not isinstance(input, unicode):
                input = unicode(input, 'utf-8')
            input = input.encode('ascii', 'ignore')
        else:
            input = ''
        newJob = createJob(request.user, application.name, optionsList,
                           commandOptions, input)
        messages.success(request, 'Success: job launched.')
        return redirect(view_job, job_id=newJob.id, resource='')
    else:
        if category:
            fromWorkbench = False
            try:

                category = \
                ApplicationCategories.objects.get(name=category)
               # compoundCount = \
               # Compound.objects.filter(user=request.user).count()
               # category.name = 'Upload' #AA

                compoundCount = 0 #AA
                print '\n here?', compoundCount
                print '\n category and compoundCount', category.name, compoundCount
                if category.name != 'Upload':
                    fromWorkbench = True
                if category.name == 'Clustering' and compoundCount < 3:
                    messages.info(request,
                                  'Notice: you must have at least 3 compounds to perform clustering. Please use this form to add more compounds and then click "Cluster" again.'
                                  )
                    return redirect('myCompounds.views.uploadCompound')
                if category.name == 'Properties' and compoundCount < 1:
                    messages.info(request,
                                  'Notice: you must have at least one compound to compute properties. Please use this form to add compounds and then click "Properties" again.'
                                  )
                    return redirect('myCompounds.views.uploadCompound')
                print '\n category.,name is', category.name
                title = 'Launch ' + category.name + ' Job'
                print '\n launch,', title
                apps = Application.objects.filter(category=category)
            except:
                print '\n in except end'
                raise Http404
        else:
            print '\n in launch job'
            title = 'Launch Job'
            apps = Application.objects.filter()
        fields = {}
        fields['application'] = ModelChoiceField(queryset=apps,
                empty_label='')
        form = type('%sForm' % 'choose application', (Form, ), fields)

        dict = {'title':title, 'form':form, 'fromWorkbench':fromWorkbench,'totlaCompounds':0}

        return render(request, 'submitForm.html',dict)



#@guest_allowed
def view_job(
    request,
    job_id,
    resource=None,
    filename=None,
    ):

    job = updateJob(request.user, job_id)
    if job == False:
        raise Http404
    if resource:
        if resource == 'delete':
            deleteJob(request.user, job.id)
            return HttpResponse('deleted', content_type='text/plain')
        if resource == 'download':
            f = open(job.output, 'r')
            result = f.read()
            f.close()
            if job.application.output_type == 'application/json.canvasxpress':
                result = re.search(r'smps":"(.*)"}},', result).group(1)
            return HttpResponse(result,
                             content_type=job.application.output_type)
    if request.is_ajax():
        if job.status == Job.RUNNING:
            response = dict(status='RUNNING')
        else:
            response = dict(status='DONE')
        return HttpResponse(dumps(response), 'text/json')
    if job.status == Job.FINISHED:
        finalResult = job.output
        finalResult = re.sub('.*/', '', finalResult, count=0)
        finalResult = '/working/' + finalResult

        # select correct viewer here based on output type

        if job.application.output_type == 'chemical/sdfUpload':
            f = open(job.output, 'r')
            sdf = f.read()
            f.close()
            result, error = batch_sdf_to_smiles(sdf) 
            quotedSmiles = []
            for smiles in result.splitlines():
                match = re.search(r'(\S+)\s+(\S+)', smiles)
                smiOnly = match.group(1)
                cid = match.group(2)
                quotedSmiles.append({'smiles': urlquote(smiOnly), 'cid':cid})

            return render(request, 'sdfUpload.html', dict(title=str(job.application) + ' Results',
                    job=job, compounds=quotedSmiles))

        if job.application.output_type == 'text/ei.search.result':
            f = open(job.output, 'r')
            csvinput = csv.reader(f, delimiter=' ')
            csvOutput = []
            for line in csvinput:
                csvOutput.append(line)
            f.close()

            return render(request,'eiresult.html',
                                      dict(title=str(job.application) + ' Results',
                                           job=job, compounds=csvOutput, query=job.input)
                                    )
        if job.application.output_type == 'text/fp.search.result':
            f = open(job.output, 'r')
            csvinput = csv.reader(f, delimiter=' ')
            csvOutput = []
            for line in csvinput:
                csvOutput.append(line)
            f.close()

            return render(request,'fpresult.html',
                                      dict(title=str(job.application) + ' Results',
                                           job=job, compounds=csvOutput, query=job.input))
        elif job.application.output_type == 'text/sdf.upload':
            f = open(job.output, 'r')
            message = f.read()
            f.close()
            deleteJob(request.user, job.id)
            if re.search(r"^ERROR:", message):
                messages.error(request, message)
                return redirect('myCompounds.views.uploadCompound')
            else:
                messages.success(request, message)
                return redirect('myCompounds.views.showCompounds',
                                resource='')
        elif job.application.output_type \
            == 'application/json.cytoscape':
            f = open(job.output, 'r')
            plotJSON = f.read()
            f.close()

            return render(request,'view_network.html',
                                      dict(title=str(job.application) + ' Results',
                                           result=finalResult, job=job, plotJSON=plotJSON))
        elif job.application.output_type \
            == 'application/json.canvasxpress':
            f = open(job.output, 'r')
            plotJSON = f.read()
            f.close()
            if (job.application.name == 'Hierarchical Clustering')\
                or (job.application.name == 'Numeric Data Clustering'):
                tree = True 

                return render(request,'view_job_oldcx.html',
                                          dict(title=str(job.application) + ' Results',
                                               result=finalResult, tree=tree, job=job, plotJSON=plotJSON)
                                          )
            else:
                tree = False

                return render(request,'view_job.html',
                                          dict(title=str(job.application) + ' Results',
                                               result=finalResult, tree=tree, job=job, plotJSON=plotJSON),
                                          )
        elif job.application.output_type == 'text/properties.table':
            f = open(job.output, 'r')
            csvinput = csv.reader(f)
            csvOutput = []
            for line in csvinput:
                csvOutput.append(line)
            f.close()

            return render(request,'view_csv.html',
                                      dict(title=str(job.application) + ' Results',
                                           result=finalResult, job=job, csv=csvOutput))
        elif job.application.output_type == 'text/bins.table':
            f = open(job.output, 'r')
            csvinput = csv.reader(f)
            bins = defaultdict(list)
            iterCsvInput = iter(csvinput)
            next(iterCsvInput)  # skip first line
            for line in iterCsvInput:
                cid = line[0]
                binSize = line[1]
                bin = line[2]
                bins[bin].append(cid)
            f.close()
            bins = OrderedDict(sorted(bins.items(), key=lambda t: \
                               int(t[0])))

            return render(request,'bins.html',
                                      dict(title=str(job.application) + ' Results',
                                           result=finalResult, job=job, bins=bins)
                                     )
        elif job.application.output_type == 'chemical/x-mdl-sdfile':
            f = open(job.output, 'r')
            sdf = f.read()
            f.close()
            nextStep = job.input
            deleteJob(request.user, job.id)
            if nextStep == 'workbench':
                newJob = createJob(request.user, 'Upload Compounds', '',
                    ['--user=' + str(request.user.id)], sdf)
                time.sleep(2)
                return redirect('tools.views.view_job', job_id=newJob.id,
                    resource='')
            elif nextStep == 'smiles':
                result, error = batch_sdf_to_smiles(sdf) 
                return HttpResponse(result,
                                 content_type=job.application.output_type)
            else:
                return HttpResponse(sdf,
                                 content_type=job.application.output_type)
        else:

            # if content_type is unknown, just send the file to the user

            return redirect(view_job, job_id=job.id, resource='download'
                            , filename='output')
    elif job.status == Job.RUNNING:

        return render(request,'wait.html',
                                  dict(title=job.application.name
                                             + ' Job Running <img src="/static/images/spinner.gif"/>'
                                       ))
    elif job.status == Job.FAILED:
        messages.error(request,
                       'Job Failed due to invalid input data and/or invalid selected options. Please double check that your uploaded data (compounds and/or numeric data), and input options are valid and try running the tool again.'
                       )

        return render(request,'view_job.html', dict(title='Error: '
                                                              + str(job.application) + ' Job Failed'
                                                        , job=job))
#AA@guest_allowed
def list_jobs(request):
    matches = getJobList(request.user)

    return render(request,'list_jobs.html', dict(matches=matches))