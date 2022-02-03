<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:rdam="http://rdaregistry.info/Elements/m/"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    version="2.0">
   
    <xsl:template match="/">
        <xsl:variable name="elements">
        <xsl:value-of select="distinct-values(//*/name())" separator=", "/>
        </xsl:variable>
        <xsl:value-of select="for $i in $elements return $i"/>
   </xsl:template> 
</xsl:stylesheet>