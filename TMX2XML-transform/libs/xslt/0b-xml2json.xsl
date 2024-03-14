<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="3.0">

    <xsl:output method="text" indent="no" omit-xml-declaration="yes" />

    <xsl:template match="body">
        <xsl:text>[</xsl:text>
        <xsl:apply-templates select="tu" />
        <xsl:text>&#xA;]</xsl:text>
    </xsl:template>

    <xsl:template match="tu">
        <xsl:text>&#xA;&#x9;{</xsl:text>
        
        <xsl:for-each select="@*">
            <xsl:text>&#xA;&#x9;&#x9;"</xsl:text>
            <xsl:value-of select="name()" />
            <xsl:text>": "</xsl:text>
            <xsl:value-of select="replace(replace(., '\\', '\\\\'), '/', '\\/')" />
            <xsl:text>",</xsl:text>
        </xsl:for-each>
        
        <xsl:text>&#xA;&#x9;&#x9;"ST": "</xsl:text>
        <xsl:apply-templates select="seg[1]" />
        <xsl:text>",</xsl:text>
        <xsl:text>&#xA;&#x9;&#x9;"TT": "</xsl:text>
        <xsl:apply-templates select="seg[2]" />
        <xsl:text>"</xsl:text>
        <xsl:text>&#xA;&#x9;}</xsl:text>
        
        <xsl:if test="following-sibling::tu">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="seg">
        <xsl:value-of select="replace(replace(replace(replace(replace(., '\\', '\\\\'), '&quot;', '&amp;quot;'), '&lt;', '&amp;lt;'), '&gt;', '&amp;gt;'), '/', '\\/')" />
    </xsl:template>

</xsl:stylesheet>
