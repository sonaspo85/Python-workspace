<?xml version="1.0"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:output method="xml" version="1.0" indent="no" encoding="UTF-8"/>
	<xsl:strip-space elements="*"/>
	<xsl:preserve-space elements="seg"/>

	<xsl:template match="/">
		<xsl:text>&#xA;</xsl:text>
		<xsl:apply-templates />
	</xsl:template>

	<xsl:template match="@* | node()">
		<xsl:copy>
			<xsl:apply-templates select="@* | node()" />
		</xsl:copy>
	</xsl:template>

	<xsl:template match="header">
		<xsl:text>&#xA;</xsl:text>
		<xsl:copy>
			<xsl:apply-templates select="@* | node()" />
		</xsl:copy>
	</xsl:template>

	<xsl:template match="body">
		<xsl:text>&#xA;</xsl:text>
		<xsl:copy>
			<xsl:apply-templates />
			<xsl:text>&#xA;</xsl:text>
		</xsl:copy>
		<xsl:text>&#xA;</xsl:text>
	</xsl:template>

	<xsl:template match="tu">
		<xsl:text>&#xA;&#x9;</xsl:text>
		<xsl:copy>
			<xsl:attribute name="creationdate">
				<xsl:value-of select="@creationdate" />
			</xsl:attribute>
			<xsl:attribute name="creationid">
				<xsl:value-of select="'TCS'" />
			</xsl:attribute>
			<xsl:apply-templates />
			<xsl:text>&#xA;&#x9;</xsl:text>
		</xsl:copy>
	</xsl:template>

	<xsl:template match="tuv">
		<xsl:text>&#xA;&#x9;&#x9;</xsl:text>
		<xsl:copy>
			<xsl:apply-templates select="@* | node()" />
			<xsl:text>&#xA;&#x9;&#x9;</xsl:text>
		</xsl:copy>
	</xsl:template>

	<xsl:template match="seg">
		<xsl:text>&#xA;&#x9;&#x9;&#x9;</xsl:text>
		<xsl:copy>
			<xsl:apply-templates select="@* | node()" />
		</xsl:copy>
	</xsl:template>

    <xsl:template match="ph/@type">
    </xsl:template>

    <xsl:template match="bpt/@i">
		<xsl:variable name="pos">
			<xsl:value-of select="count(parent::*/preceding-sibling::bpt) + 1" />
		</xsl:variable>
        <xsl:attribute name="{local-name()}">
            <xsl:value-of select="$pos"/>
        </xsl:attribute>
    </xsl:template>

    <xsl:template match="bpt/@type">
		<xsl:choose>
			<xsl:when test="starts-with(., 'x-LockedContent')">
				<xsl:attribute name="type" select="."/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:attribute name="type">1</xsl:attribute>
			</xsl:otherwise>
		</xsl:choose>
    </xsl:template>

    <xsl:template match="ept/@i">
		<xsl:variable name="pos">
			<xsl:choose>
				<xsl:when test="not(parent::*/preceding-sibling::*[1][matches(name(), '^bpt|ph$')])">
					<xsl:value-of select="'unknown'" />
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="count(parent::*/preceding-sibling::bpt)" />
				</xsl:otherwise>
			</xsl:choose>
		</xsl:variable>
        <xsl:attribute name="{local-name()}">
            <xsl:value-of select="$pos"/>
        </xsl:attribute>
    </xsl:template>

	<xsl:template match="text()" priority="10">
		<xsl:analyze-string select="." regex="&lt;C_Image&gt;.*&lt;/C_Image&gt;">
			<xsl:matching-substring>
			</xsl:matching-substring>
			<xsl:non-matching-substring>
				<xsl:value-of select="replace(., '(~~)$', '$1&#x20;')"/>
			</xsl:non-matching-substring>
		</xsl:analyze-string>
	</xsl:template>

</xsl:stylesheet>