<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:rdam="http://rdaregistry.info/Elements/m/"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
    version="2.0">
    <xsl:variable name="coll" select="collection('?select=*.xml')"/>
    <xsl:template match="/">
        <rdf:RDF>
            <xsl:for-each select="$coll/rdf:RDF/rdf:Description">
                    <xsl:call-template name="identity"/>
        </xsl:for-each>
        </rdf:RDF>
    </xsl:template>
    <xsl:template name="identity">
        <xsl:copy-of select="."/>
    </xsl:template>
</xsl:stylesheet>