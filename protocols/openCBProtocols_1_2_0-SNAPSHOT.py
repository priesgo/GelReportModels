"""
DO NOT EDIT THIS FILE!!
This file is automatically generated by the process_schemas.py program
in the scripts directory. It is not intended to be edited directly. If
you need to update the GEL protocol classes, please run the script
on the appropriate schema version.
"""
from protocols.protocol import ProtocolElement
from protocols.protocol import SearchRequest
from protocols.protocol import SearchResponse

import avro.schema

version = '3.0.0'


class AdditionalAttribute(ProtocolElement):
    """
    No documentation
    """
    _schemaSource = """
{"namespace": "org.opencb.biodata.models.variant.avro", "type":
"record", "name": "AdditionalAttribute", "fields": [{"type":
{"values": "string", "type": "map"}, "name": "attribute"}]}
"""
    schema = avro.schema.parse(_schemaSource)
    requiredFields = {
        "attribute",
    }

    @classmethod
    def isEmbeddedType(cls, fieldName):
        embeddedTypes = {}
        return fieldName in embeddedTypes

    @classmethod
    def getEmbeddedType(cls, fieldName):
        embeddedTypes = {}

        return embeddedTypes[fieldName]

    __slots__ = [
        'attribute'
    ]

    def __init__(self, **kwargs):
        self.attribute = kwargs.get(
            'attribute', None)


class Aggregation(object):
    """
    No documentation
    """
    NONE = "NONE"
    BASIC = "BASIC"
    EVS = "EVS"
    EXAC = "EXAC"


class AlleleOrigin(object):
    """
    Variant origin.  * `SO_0001781`: de novo variant.
    http://purl.obolibrary.org/obo/SO_0001781 * `SO_0001778`: germline
    variant. http://purl.obolibrary.org/obo/SO_0001778 * `SO_0001775`:
    maternal variant. http://purl.obolibrary.org/obo/SO_0001775 *
    `SO_0001776`: paternal variant.
    http://purl.obolibrary.org/obo/SO_0001776 * `SO_0001779`: pedigree
    specific variant. http://purl.obolibrary.org/obo/SO_0001779 *
    `SO_0001780`: population specific variant.
    http://purl.obolibrary.org/obo/SO_0001780 * `SO_0001777`: somatic
    variant. http://purl.obolibrary.org/obo/SO_0001777
    """
    SO_0001781 = "SO_0001781"
    SO_0001778 = "SO_0001778"
    SO_0001775 = "SO_0001775"
    SO_0001776 = "SO_0001776"
    SO_0001779 = "SO_0001779"
    SO_0001780 = "SO_0001780"
    SO_0001777 = "SO_0001777"


class AllelesCode(object):
    """
    No documentation
    """
    ALLELES_OK = "ALLELES_OK"
    ALLELES_MISSING = "ALLELES_MISSING"
    MULTIPLE_ALTERNATES = "MULTIPLE_ALTERNATES"
    HAPLOID = "HAPLOID"


class AlternateCoordinate(ProtocolElement):
    """
    No documentation
    """
    _schemaSource = """
{"namespace": "org.opencb.biodata.models.variant.avro", "type":
"record", "name": "AlternateCoordinate", "fields": [{"type": ["null",
"string"], "name": "chromosome"}, {"doc": "", "type": ["null", "int"],
"name": "start"}, {"doc": "", "type": ["null", "int"], "name": "end"},
{"doc": "", "type": ["null", "string"], "name": "reference"}, {"doc":
"", "type": "string", "name": "alternate"}, {"type": {"symbols":
["SNV", "SNP", "MNV", "MNP", "INDEL", "SV", "INSERTION", "DELETION",
"TRANSLOCATION", "INVERSION", "CNV", "NO_VARIATION", "SYMBOLIC",
"MIXED"], "doc": "", "type": "enum", "name": "VariantType"}, "name":
"type"}]}
"""
    schema = avro.schema.parse(_schemaSource)
    requiredFields = {
        "alternate",
        "chromosome",
        "end",
        "reference",
        "start",
        "type",
    }

    @classmethod
    def isEmbeddedType(cls, fieldName):
        embeddedTypes = {}
        return fieldName in embeddedTypes

    @classmethod
    def getEmbeddedType(cls, fieldName):
        embeddedTypes = {}

        return embeddedTypes[fieldName]

    __slots__ = [
        'alternate', 'chromosome', 'end', 'reference', 'start', 'type'
    ]

    def __init__(self, **kwargs):
        self.alternate = kwargs.get(
            'alternate', 'None')
        self.chromosome = kwargs.get(
            'chromosome', None)
        self.end = kwargs.get(
            'end', None)
        self.reference = kwargs.get(
            'reference', None)
        self.start = kwargs.get(
            'start', None)
        self.type = kwargs.get(
            'type', None)


class ClinVar(ProtocolElement):
    """
    No documentation
    """
    _schemaSource = """
{"namespace": "org.opencb.biodata.models.variant.avro", "type":
"record", "name": "ClinVar", "fields": [{"type": "string", "name":
"accession"}, {"type": "string", "name": "clinicalSignificance"},
{"type": {"items": "string", "type": "array"}, "name": "traits"},
{"type": {"items": "string", "type": "array"}, "name": "geneNames"},
{"type": "string", "name": "reviewStatus"}]}
"""
    schema = avro.schema.parse(_schemaSource)
    requiredFields = {
        "accession",
        "clinicalSignificance",
        "geneNames",
        "reviewStatus",
        "traits",
    }

    @classmethod
    def isEmbeddedType(cls, fieldName):
        embeddedTypes = {}
        return fieldName in embeddedTypes

    @classmethod
    def getEmbeddedType(cls, fieldName):
        embeddedTypes = {}

        return embeddedTypes[fieldName]

    __slots__ = [
        'accession', 'clinicalSignificance', 'geneNames',
        'reviewStatus', 'traits'
    ]

    def __init__(self, **kwargs):
        self.accession = kwargs.get(
            'accession', 'None')
        self.clinicalSignificance = kwargs.get(
            'clinicalSignificance', 'None')
        self.geneNames = kwargs.get(
            'geneNames', None)
        self.reviewStatus = kwargs.get(
            'reviewStatus', 'None')
        self.traits = kwargs.get(
            'traits', None)


class ClinicalSignificance(object):
    """
