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

    <xsl:template match="ept[@i='unknown'][count(preceding-sibling::bpt) = count(preceding-sibling::ept)]" priority="10">
    </xsl:template>

    <xsl:template match="ept">
    	<xsl:copy>
	    	<xsl:choose>
	    		<xsl:when test="@i = 'unknown'">
	    			<xsl:variable name="start" select="preceding-sibling::bpt[preceding-sibling::*[1][matches(name(), '^bpt|ph$')]][1]/@i"/>
			    	<xsl:variable name="end" select="preceding-sibling::ept[preceding-sibling::*[1][matches(name(), '^bpt|ph$')]][1]/@i"/>
					<xsl:variable name="nested" select="$end - $start + 1"/>
					<xsl:choose>
						<xsl:when test="preceding-sibling::node()[1][self::text()] and 
										preceding-sibling::*[1][self::ept][@i!='unknown'] and
										parent::seg/*[1][name()='ph']">
							<xsl:attribute name="i" select="$end - $nested - 1"/>
						</xsl:when>
						<xsl:when test="preceding-sibling::*[1][self::ept][@i='unknown'] and
										preceding-sibling::*[2][self::ept][@i='unknown'] and
										preceding-sibling::*[3][self::ept][@i='unknown'] and
										preceding-sibling::*[4][self::ept][@i='unknown'] and
										preceding-sibling::*[5][self::ept][@i='unknown'] and
										preceding-sibling::*[6][self::ept][@i='unknown'] and
										preceding-sibling::*[7][self::ept][@i='unknown'] and
										preceding-sibling::*[8][self::ept][@i='unknown'] and
										preceding-sibling::*[9][self::ept][@i='unknown']">
			    			<xsl:attribute name="i" select="$end - $nested - 9"/>
						</xsl:when>
						<xsl:when test="preceding-sibling::*[1][self::ept][@i='unknown'] and
										preceding-sibling::*[2][self::ept][@i='unknown'] and
										preceding-sibling::*[3][self::ept][@i='unknown'] and
										preceding-sibling::*[4][self::ept][@i='unknown'] and
										preceding-sibling::*[5][self::ept][@i='unknown'] and
										preceding-sibling::*[6][self::ept][@i='unknown'] and
										preceding-sibling::*[7][self::ept][@i='unknown'] and
										preceding-sibling::*[8][self::ept][@i='unknown']">
			    			<xsl:attribute name="i" select="$end - $nested - 8"/>
						</xsl:when>
						<xsl:when test="preceding-sibling::*[1][self::ept][@i='unknown'] and
										preceding-sibling::*[2][self::ept][@i='unknown'] and
										preceding-sibling::*[3][self::ept][@i='unknown'] and
										preceding-sibling::*[4][self::ept][@i='unknown'] and
										preceding-sibling::*[5][self::ept][@i='unknown'] and
										preceding-sibling::*[6][self::ept][@i='unknown'] and
										preceding-sibling::*[7][self::ept][@i='unknown']">
			    			<xsl:attribute name="i" select="$end - $nested - 7"/>
						</xsl:when>
						<xsl:when test="preceding-sibling::*[1][self::ept][@i='unknown'] and
										preceding-sibling::*[2][self::ept][@i='unknown'] and
										preceding-sibling::*[3][self::ept][@i='unknown'] and
										preceding-sibling::*[4][self::ept][@i='unknown'] and
										preceding-sibling::*[5][self::ept][@i='unknown'] and
										preceding-sibling::*[6][self::ept][@i='unknown']">
			    			<xsl:attribute name="i" select="$end - $nested - 6"/>
						</xsl:when>
						<xsl:when test="preceding-sibling::*[1][self::ept][@i='unknown'] and
										preceding-sibling::*[2][self::ept][@i='unknown'] and
										preceding-sibling::*[3][self::ept][@i='unknown'] and
										preceding-sibling::*[4][self::ept][@i='unknown'] and
										preceding-sibling::*[5][self::ept][@i='unknown']">
			    			<xsl:attribute name="i" select="$end - $nested - 5"/>
						</xsl:when>
						<xsl:when test="preceding-sibling::*[1][self::ept][@i='unknown'] and
										preceding-sibling::*[2][self::ept][@i='unknown'] and
										preceding-sibling::*[3][self::ept][@i='unknown'] and
										preceding-sibling::*[4][self::ept][@i='unknown']">
			    			<xsl:attribute name="i" select="$end - $nested - 4"/>
						</xsl:when>
						<xsl:when test="preceding-sibling::*[1][self::ept][@i='unknown'] and
										preceding-sibling::*[2][self::ept][@i='unknown'] and
										preceding-sibling::*[3][self::ept][@i='unknown']">
			    			<xsl:attribute name="i" select="$end - $nested - 3"/>
						</xsl:when>
						<xsl:when test="preceding-sibling::*[1][self::ept][@i='unknown'] and 
										preceding-sibling::*[2][self::ept][@i='unknown']">
			    			<xsl:attribute name="i" select="$end - $nested - 2"/>
						</xsl:when>
						<xsl:when test="preceding-sibling::*[1][self::ept][@i='unknown']">
			    			<xsl:attribute name="i" select="$end - $nested - 1"/>
						</xsl:when>
						<xsl:when test="preceding-sibling::*[1][self::ept][@i!='unknown']">
			    			<xsl:attribute name="i" select="$end - $nested"/>
						</xsl:when>
						<xsl:otherwise>
			    			<xsl:attribute name="i" select="@i"/>
						</xsl:otherwise>
					</xsl:choose>
	    		</xsl:when>
	    		<xsl:otherwise>
	    			<xsl:attribute name="i" select="@i"/>
	    		</xsl:otherwise>
	    	</xsl:choose>
	    </xsl:copy>
    </xsl:template>

</xsl:stylesheet>