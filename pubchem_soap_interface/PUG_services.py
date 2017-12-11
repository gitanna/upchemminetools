################################################## 
# PUG_services.py 
# generated by ZSI.generate.wsdl2python
##################################################


from PUG_services_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
import ZSI
from ZSI.generate.pyclass import pyclass_type

# Locator
class PUGLocator:
    PUGSoap_address = "http://127.0.0.1:9000/pug_soap/pug_soap.cgi"
    def getPUGSoapAddress(self):
        return PUGLocator.PUGSoap_address
    def getPUGSoap(self, url=None, **kw):
        return PUGSoapSOAP(url or PUGLocator.PUGSoap_address, **kw)

# Methods
class PUGSoapSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: AssayDownload
    def AssayDownload(self, request):
        if isinstance(request, AssayDownloadSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/AssayDownload", **kw)
        # no output wsaction
        response = self.binding.Receive(AssayDownloadSoapOut.typecode)
        return response

    # op: Download
    def Download(self, request):
        if isinstance(request, DownloadSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/Download", **kw)
        # no output wsaction
        response = self.binding.Receive(DownloadSoapOut.typecode)
        return response

    # op: GetAssayColumnDescription
    def GetAssayColumnDescription(self, request):
        if isinstance(request, GetAssayColumnDescriptionSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/GetAssayColumnDescription", **kw)
        # no output wsaction
        response = self.binding.Receive(GetAssayColumnDescriptionSoapOut.typecode)
        return response

    # op: GetAssayColumnDescriptions
    def GetAssayColumnDescriptions(self, request):
        if isinstance(request, GetAssayColumnDescriptionsSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/GetAssayColumnDescriptions", **kw)
        # no output wsaction
        response = self.binding.Receive(GetAssayColumnDescriptionsSoapOut.typecode)
        return response

    # op: GetAssayDescription
    def GetAssayDescription(self, request):
        if isinstance(request, GetAssayDescriptionSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/GetAssayDescription", **kw)
        # no output wsaction
        response = self.binding.Receive(GetAssayDescriptionSoapOut.typecode)
        return response

    # op: GetDownloadUrl
    def GetDownloadUrl(self, request):
        if isinstance(request, GetDownloadUrlSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/GetDownloadUrl", **kw)
        # no output wsaction
        response = self.binding.Receive(GetDownloadUrlSoapOut.typecode)
        return response

    # op: GetEntrezKey
    def GetEntrezKey(self, request):
        if isinstance(request, GetEntrezKeySoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/GetEntrezKey", **kw)
        # no output wsaction
        response = self.binding.Receive(GetEntrezKeySoapOut.typecode)
        return response

    # op: GetEntrezUrl
    def GetEntrezUrl(self, request):
        if isinstance(request, GetEntrezUrlSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/GetEntrezUrl", **kw)
        # no output wsaction
        response = self.binding.Receive(GetEntrezUrlSoapOut.typecode)
        return response

    # op: GetIDList
    def GetIDList(self, request):
        if isinstance(request, GetIDListSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/GetIDList", **kw)
        # no output wsaction
        response = self.binding.Receive(GetIDListSoapOut.typecode)
        return response

    # op: GetListItemsCount
    def GetListItemsCount(self, request):
        if isinstance(request, GetListItemsCountSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/GetListItemsCount", **kw)
        # no output wsaction
        response = self.binding.Receive(GetListItemsCountSoapOut.typecode)
        return response

    # op: GetOperationStatus
    def GetOperationStatus(self, request):
        if isinstance(request, GetOperationStatusSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/GetOperationStatus", **kw)
        # no output wsaction
        response = self.binding.Receive(GetOperationStatusSoapOut.typecode)
        return response

    # op: GetStandardizedCID
    def GetStandardizedCID(self, request):
        if isinstance(request, GetStandardizedCIDSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/GetStandardizedCID", **kw)
        # no output wsaction
        response = self.binding.Receive(GetStandardizedCIDSoapOut.typecode)
        return response

    # op: GetStandardizedStructure
    def GetStandardizedStructure(self, request):
        if isinstance(request, GetStandardizedStructureSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/GetStandardizedStructure", **kw)
        # no output wsaction
        response = self.binding.Receive(GetStandardizedStructureSoapOut.typecode)
        return response

    # op: GetStandardizedStructureBase64
    def GetStandardizedStructureBase64(self, request):
        if isinstance(request, GetStandardizedStructureBase64SoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/GetStandardizedStructureBase64", **kw)
        # no output wsaction
        response = self.binding.Receive(GetStandardizedStructureBase64SoapOut.typecode)
        return response

    # op: GetStatusMessage
    def GetStatusMessage(self, request):
        if isinstance(request, GetStatusMessageSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/GetStatusMessage", **kw)
        # no output wsaction
        response = self.binding.Receive(GetStatusMessageSoapOut.typecode)
        return response

    # op: IdentitySearch
    def IdentitySearch(self, request):
        if isinstance(request, IdentitySearchSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/IdentitySearch", **kw)
        # no output wsaction
        response = self.binding.Receive(IdentitySearchSoapOut.typecode)
        return response

    # op: IDExchange
    def IDExchange(self, request):
        if isinstance(request, IDExchangeSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/IDExchange", **kw)
        # no output wsaction
        response = self.binding.Receive(IDExchangeSoapOut.typecode)
        return response

    # op: InputAssay
    def InputAssay(self, request):
        if isinstance(request, InputAssaySoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/InputAssay", **kw)
        # no output wsaction
        response = self.binding.Receive(InputAssaySoapOut.typecode)
        return response

    # op: InputEntrez
    def InputEntrez(self, request):
        if isinstance(request, InputEntrezSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/InputEntrez", **kw)
        # no output wsaction
        response = self.binding.Receive(InputEntrezSoapOut.typecode)
        return response

    # op: InputList
    def InputList(self, request):
        if isinstance(request, InputListSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/InputList", **kw)
        # no output wsaction
        response = self.binding.Receive(InputListSoapOut.typecode)
        return response

    # op: InputListString
    def InputListString(self, request):
        if isinstance(request, InputListStringSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/InputListString", **kw)
        # no output wsaction
        response = self.binding.Receive(InputListStringSoapOut.typecode)
        return response

    # op: InputListText
    def InputListText(self, request):
        if isinstance(request, InputListTextSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/InputListText", **kw)
        # no output wsaction
        response = self.binding.Receive(InputListTextSoapOut.typecode)
        return response

    # op: InputStructure
    def InputStructure(self, request):
        if isinstance(request, InputStructureSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/InputStructure", **kw)
        # no output wsaction
        response = self.binding.Receive(InputStructureSoapOut.typecode)
        return response

    # op: InputStructureBase64
    def InputStructureBase64(self, request):
        if isinstance(request, InputStructureBase64SoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/InputStructureBase64", **kw)
        # no output wsaction
        response = self.binding.Receive(InputStructureBase64SoapOut.typecode)
        return response

    # op: MFSearch
    def MFSearch(self, request):
        if isinstance(request, MFSearchSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/MFSearch", **kw)
        # no output wsaction
        response = self.binding.Receive(MFSearchSoapOut.typecode)
        return response

    # op: ScoreMatrix
    def ScoreMatrix(self, request):
        if isinstance(request, ScoreMatrixSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/ScoreMatrix", **kw)
        # no output wsaction
        response = self.binding.Receive(ScoreMatrixSoapOut.typecode)
        return response

    # op: SimilaritySearch2D
    def SimilaritySearch2D(self, request):
        if isinstance(request, SimilaritySearch2DSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/SimilaritySearch2D", **kw)
        # no output wsaction
        response = self.binding.Receive(SimilaritySearch2DSoapOut.typecode)
        return response

    # op: Standardize
    def Standardize(self, request):
        if isinstance(request, StandardizeSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/Standardize", **kw)
        # no output wsaction
        response = self.binding.Receive(StandardizeSoapOut.typecode)
        return response

    # op: SubstructureSearch
    def SubstructureSearch(self, request):
        if isinstance(request, SubstructureSearchSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/SubstructureSearch", **kw)
        # no output wsaction
        response = self.binding.Receive(SubstructureSearchSoapOut.typecode)
        return response

    # op: SuperstructureSearch
    def SuperstructureSearch(self, request):
        if isinstance(request, SuperstructureSearchSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://127.0.0.1:9000/SuperstructureSearch", **kw)
        # no output wsaction
        response = self.binding.Receive(SuperstructureSearchSoapOut.typecode)
        return response

AssayDownloadSoapIn = ns0.AssayDownload_Dec().pyclass

AssayDownloadSoapOut = ns0.AssayDownloadResponse_Dec().pyclass

DownloadSoapIn = ns0.Download_Dec().pyclass

DownloadSoapOut = ns0.DownloadResponse_Dec().pyclass

GetAssayColumnDescriptionSoapIn = ns0.GetAssayColumnDescription_Dec().pyclass

GetAssayColumnDescriptionSoapOut = ns0.GetAssayColumnDescriptionResponse_Dec().pyclass

GetAssayColumnDescriptionsSoapIn = ns0.GetAssayColumnDescriptions_Dec().pyclass

GetAssayColumnDescriptionsSoapOut = ns0.GetAssayColumnDescriptionsResponse_Dec().pyclass

GetAssayDescriptionSoapIn = ns0.GetAssayDescription_Dec().pyclass

GetAssayDescriptionSoapOut = ns0.GetAssayDescriptionResponse_Dec().pyclass

GetDownloadUrlSoapIn = ns0.GetDownloadUrl_Dec().pyclass

GetDownloadUrlSoapOut = ns0.GetDownloadUrlResponse_Dec().pyclass

GetEntrezKeySoapIn = ns0.GetEntrezKey_Dec().pyclass

GetEntrezKeySoapOut = ns0.GetEntrezKeyResponse_Dec().pyclass

GetEntrezUrlSoapIn = ns0.GetEntrezUrl_Dec().pyclass

GetEntrezUrlSoapOut = ns0.GetEntrezUrlResponse_Dec().pyclass

GetIDListSoapIn = ns0.GetIDList_Dec().pyclass

GetIDListSoapOut = ns0.GetIDListResponse_Dec().pyclass

GetListItemsCountSoapIn = ns0.GetListItemsCount_Dec().pyclass

GetListItemsCountSoapOut = ns0.GetListItemsCountResponse_Dec().pyclass

GetOperationStatusSoapIn = ns0.GetOperationStatus_Dec().pyclass

GetOperationStatusSoapOut = ns0.GetOperationStatusResponse_Dec().pyclass

GetStandardizedCIDSoapIn = ns0.GetStandardizedCID_Dec().pyclass

GetStandardizedCIDSoapOut = ns0.GetStandardizedCIDResponse_Dec().pyclass

GetStandardizedStructureSoapIn = ns0.GetStandardizedStructure_Dec().pyclass

GetStandardizedStructureSoapOut = ns0.GetStandardizedStructureResponse_Dec().pyclass

GetStandardizedStructureBase64SoapIn = ns0.GetStandardizedStructureBase64_Dec().pyclass

GetStandardizedStructureBase64SoapOut = ns0.GetStandardizedStructureBase64Response_Dec().pyclass

GetStatusMessageSoapIn = ns0.GetStatusMessage_Dec().pyclass

GetStatusMessageSoapOut = ns0.GetStatusMessageResponse_Dec().pyclass

IdentitySearchSoapIn = ns0.IdentitySearch_Dec().pyclass

IdentitySearchSoapOut = ns0.IdentitySearchResponse_Dec().pyclass

IDExchangeSoapIn = ns0.IDExchange_Dec().pyclass

IDExchangeSoapOut = ns0.IDExchangeResponse_Dec().pyclass

InputAssaySoapIn = ns0.InputAssay_Dec().pyclass

InputAssaySoapOut = ns0.InputAssayResponse_Dec().pyclass

InputEntrezSoapIn = ns0.InputEntrez_Dec().pyclass

InputEntrezSoapOut = ns0.InputEntrezResponse_Dec().pyclass

InputListSoapIn = ns0.InputList_Dec().pyclass

InputListSoapOut = ns0.InputListResponse_Dec().pyclass

InputListStringSoapIn = ns0.InputListString_Dec().pyclass

InputListStringSoapOut = ns0.InputListStringResponse_Dec().pyclass

InputListTextSoapIn = ns0.InputListText_Dec().pyclass

InputListTextSoapOut = ns0.InputListTextResponse_Dec().pyclass

InputStructureSoapIn = ns0.InputStructure_Dec().pyclass

InputStructureSoapOut = ns0.InputStructureResponse_Dec().pyclass

InputStructureBase64SoapIn = ns0.InputStructureBase64_Dec().pyclass

InputStructureBase64SoapOut = ns0.InputStructureBase64Response_Dec().pyclass

MFSearchSoapIn = ns0.MFSearch_Dec().pyclass

MFSearchSoapOut = ns0.MFSearchResponse_Dec().pyclass

ScoreMatrixSoapIn = ns0.ScoreMatrix_Dec().pyclass

ScoreMatrixSoapOut = ns0.ScoreMatrixResponse_Dec().pyclass

SimilaritySearch2DSoapIn = ns0.SimilaritySearch2D_Dec().pyclass

SimilaritySearch2DSoapOut = ns0.SimilaritySearch2DResponse_Dec().pyclass

StandardizeSoapIn = ns0.Standardize_Dec().pyclass

StandardizeSoapOut = ns0.StandardizeResponse_Dec().pyclass

SubstructureSearchSoapIn = ns0.SubstructureSearch_Dec().pyclass

SubstructureSearchSoapOut = ns0.SubstructureSearchResponse_Dec().pyclass

SuperstructureSearchSoapIn = ns0.SuperstructureSearch_Dec().pyclass

SuperstructureSearchSoapOut = ns0.SuperstructureSearchResponse_Dec().pyclass