<xsl:stylesheet version="2.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
	xmlns:xs="http://www.w3.org/2001/XMLSchema" 
	exclude-result-prefixes="xs">

	<xsl:character-map name="map">
		<xsl:output-character character="&quot;" string="&amp;quot;"/>
	</xsl:character-map>

	<xsl:output method="xml" indent="no" omit-xml-declaration="yes" use-character-maps="map"/>
	<xsl:strip-space elements="*" />
	<xsl:preserve-space elements="seg" />
 
	<xsl:template match="@* | node()">
		<xsl:copy>
			<xsl:apply-templates select="@* | node()" />
		</xsl:copy>
	</xsl:template>

	<xsl:template match="/">
		<xsl:apply-templates select="tmx/body"/>
	</xsl:template>

	<xsl:template match="body">
		<body>
			<xsl:apply-templates select="tu"/>
			<xsl:text>&#xA;</xsl:text>
		</body>
	</xsl:template>

	<xsl:template match="tu">
		<xsl:text>&#xA;&#x9;</xsl:text>
		<xsl:copy>
			<xsl:apply-templates select="@* | node()" />
			<xsl:text>&#xA;&#x9;</xsl:text>
		</xsl:copy>
	</xsl:template>

	<xsl:template match="tuv">
		<xsl:apply-templates/>
	</xsl:template>

	<xsl:template match="seg">
		<xsl:text>&#xA;&#x9;&#x9;</xsl:text>
		<seg lang="{parent::tuv/@xml:lang}">
			<xsl:apply-templates/>
		</seg>
	</xsl:template>

	<xsl:template match="bpt">
		<xsl:variable name="i" select="@i" />
		<xsl:text>&lt;span class=&quot;stag&quot;&gt;</xsl:text>
		<xsl:value-of select="concat('&lt;img src=&quot;', concat('flag/', $i, '.png'), '&quot;/&gt;')"/>
		<xsl:text>&lt;/span&gt;</xsl:text>
	</xsl:template>
  
	<xsl:template match="ept">
		<xsl:variable name="i" select="@i" />
		<xsl:text>&lt;span class=&quot;stag&quot;&gt;</xsl:text>
		<xsl:value-of select="concat('&lt;img src=&quot;', concat('flag/', $i, '.png'), '&quot;/&gt;')"/>
		<xsl:text>&lt;/span&gt;</xsl:text>
	</xsl:template>
  
	<xsl:template match="ph">
		<xsl:text>&lt;span class=&quot;pic&quot;&gt;&lt;/span&gt;</xsl:text>
	</xsl:template>

	<xsl:template match="text()" priority="20">
	    <!--<xsl:variable name="str0" select="replace(., '\s+', '&#x20;')"/>-->
	    <xsl:variable name="str0" select="replace(replace(replace(., '&#xD;', ''), '&#xa;', ''), '&#x9;', '&#x20;')"/>
	    
		<xsl:analyze-string select="$str0" regex="(&lt;style.*languagevariable.*&gt;)(.*)(&lt;/languagevariable.*/style&gt;)">
			<xsl:matching-substring>
				<span class="ftag"><xsl:value-of select="regex-group(1)"/></span>
				<xsl:value-of select="regex-group(2)"/>
				<span class="ftag"><xsl:value-of select="regex-group(3)"/></span>
			</xsl:matching-substring>
		    
			<xsl:non-matching-substring>
				<xsl:analyze-string select="." regex="(&lt;languagevariable.*&gt;)(.*)(&lt;/languagevariable&gt;)">
					<xsl:matching-substring>
						<span class="ftag"><xsl:value-of select="regex-group(1)"/></span>
						<xsl:value-of select="regex-group(2)"/>
						<span class="ftag"><xsl:value-of select="regex-group(3)"/></span>
					</xsl:matching-substring>
				    
					<xsl:non-matching-substring>
						<xsl:value-of select="replace(replace(replace(., '^gt$', '&amp;gt;'), '&lt;', '###lt;'), '&gt;', '###gt;')"/>
					</xsl:non-matching-substring>
				</xsl:analyze-string>
			</xsl:non-matching-substring>
		</xsl:analyze-string>
	</xsl:template>

</xsl:stylesheet>