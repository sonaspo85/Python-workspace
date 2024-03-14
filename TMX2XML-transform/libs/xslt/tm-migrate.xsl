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

	<xsl:template match="prop">
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

	<xsl:template match="bpt">
		<xsl:choose>
			<xsl:when test="following-sibling::node()[1][self::bpt] and following-sibling::node()[2][self::text()][matches(., '^[→←]|[►◄]|:$')]">
			</xsl:when>
			<xsl:when test="following-sibling::node()[1][self::text()][matches(., '^[→←]|[►◄]|:$')]">
			</xsl:when>

			<!-- new -->
			<!-- <xsl:when test="following-sibling::node()[1][self::text()][matches(., '^Wi\-Fi$')]">
			</xsl:when> -->
			<xsl:when test="following-sibling::node()[1][self::ph] and following-sibling::node()[2][self::text()][matches(., '^Wi\-Fi$')]">
			</xsl:when>
			<!--
			<xsl:when test="following-sibling::node()[1][self::text()][matches(., '^\w+\-\w+$')]">
			</xsl:when>
			<xsl:when test="following-sibling::node()[1][self::ph] and following-sibling::node()[2][self::text()][matches(., '^\w+\-\w+$')]">
			</xsl:when>
			-->

			<xsl:when test="following-sibling::node()[1][self::text()][matches(., '^\d+\s+\w+$')] or following-sibling::node()[1][self::text()][matches(., '^\w+\s+\d+$')]">
			</xsl:when>
			<xsl:when test="following-sibling::node()[1][self::text()] and following-sibling::node()[2][self::bpt][starts-with(@type,'x-LockedContent')] and following-sibling::node()[3][self::ept]">
			</xsl:when>
			<xsl:when test="following-sibling::node()[1][self::bpt][starts-with(@type,'x-LockedContent')] and following-sibling::node()[2][self::ept]">
			</xsl:when>
			<xsl:when test="following-sibling::node()[1][self::ph] and following-sibling::node()[2][self::ept]">
			</xsl:when>
			<xsl:when test="following-sibling::node()[1][self::bpt] and following-sibling::node()[2][self::text()] and following-sibling::node()[3][self::ept] and following-sibling::node()[4][self::ept]">
			</xsl:when>
			<xsl:when test="preceding-sibling::node()[1][self::bpt] and following-sibling::node()[1][self::text()] and following-sibling::node()[2][self::ept] and following-sibling::node()[3][self::ept]">
			</xsl:when>
			<xsl:otherwise>
				<xsl:copy>
					<xsl:apply-templates select="@* | node()" />
				</xsl:copy>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template match="ept">
		<xsl:variable name="i" select="@i"/>
		<xsl:choose>
			<xsl:when test="preceding-sibling::node()[1][self::text()][matches(., '^）$')] and preceding-sibling::node()[2][self::ept] and preceding-sibling::node()[3][self::bpt][starts-with(@type, 'x-LockedContent')] and preceding-sibling::node()[4][self::text()][matches(., '^（$')] and preceding-sibling::node()[5][self::bpt]">
			</xsl:when>
			<xsl:when test="preceding-sibling::node()[3][self::text()][matches(., '^µ$')]">
			</xsl:when>
			<xsl:when test="preceding-sibling::bpt[@i=$i]/following-sibling::node()[1][self::bpt] and preceding-sibling::bpt[@i=$i]/following-sibling::node()[2][self::text()][matches(., '^→|►|:$')]">
			</xsl:when>
			<xsl:when test="preceding-sibling::node()[1][self::text()][matches(., '^[→←]|[►◄]|:$')]">
			</xsl:when>

			<!-- new -->
			<!-- <xsl:when test="preceding-sibling::node()[1][self::text()][matches(., '^Wi\-Fi$')]">
			</xsl:when> -->
			<!--
			<xsl:when test="preceding-sibling::node()[1][self::text()][matches(., '^\w+\-\w+$')]">
			</xsl:when>
			-->

			<xsl:when test="preceding-sibling::node()[1][self::text()][matches(., '^\d+\s+\w+$')] or preceding-sibling::node()[1][self::text()][matches(., '^\w+\s+\d+$')]">
			</xsl:when>
			<xsl:when test="preceding-sibling::node()[4][self::bpt] and preceding-sibling::node()[3][self::bpt] and	preceding-sibling::node()[2][self::ept] and preceding-sibling::node()[1][self::text()]">
			</xsl:when>
			<xsl:when test="preceding-sibling::node()[3][self::bpt][starts-with(@type, 'x-LockedContent')] and preceding-sibling::node()[2][self::ept] and preceding-sibling::node()[1][self::text()][.=')']">
			</xsl:when>
			<xsl:when test="preceding-sibling::node()[2][self::bpt][starts-with(@type, 'x-LockedContent')] and preceding-sibling::node()[1][self::ept]">
			</xsl:when>
			<xsl:when test="preceding-sibling::node()[3][self::bpt] and preceding-sibling::node()[2][self::bpt][starts-with(@type, 'x-LockedContent')] and  preceding-sibling::node()[1][self::ept]">
			</xsl:when>
			<xsl:when test="preceding-sibling::node()[1][self::ph] and preceding-sibling::node()[2][self::bpt]">
			</xsl:when>
			<xsl:when test="preceding-sibling::node()[3][self::bpt] and preceding-sibling::node()[2][self::bpt] and preceding-sibling::node()[1][self::text()] and following-sibling::node()[1][self::ept]">
			</xsl:when>
			<xsl:when test="preceding-sibling::node()[4][self::bpt] and preceding-sibling::node()[3][self::bpt] and preceding-sibling::node()[2][self::text()] and preceding-sibling::node()[1][self::ept]">
			</xsl:when>
			<xsl:otherwise>
				<xsl:copy>
					<xsl:apply-templates select="@* | node()" />
				</xsl:copy>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<xsl:template match="text()" priority="10">
		<xsl:choose>
			<xsl:when test="matches(., '^[→←]$')">
				<xsl:value-of select="'~~'"/>
			</xsl:when>
			<xsl:when test="matches(., '^[►◄]$')">
				<xsl:value-of select="."/>
			</xsl:when>
			<xsl:when test=".=':'">
				<xsl:value-of select="':'"/>
			</xsl:when>
			<xsl:when test="preceding-sibling::node()[2][self::bpt] and preceding-sibling::node()[1][self::bpt] and following-sibling::node()[1][self::ept] and following-sibling::node()[2][self::ept]">
				<ph x="1" type="1"/>
			</xsl:when>
			<xsl:when test="matches(., '^\d+\s+\w+$') or matches(., '^\w+\s+\d+$')">
				<xsl:value-of select="."/>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="."/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

</xsl:stylesheet>