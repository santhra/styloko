#!/usr/bin/env python
# -*- coding: utf-8 -*-
COUNTRY_CODES = [
u"AD",    #Andorra 1974    .ad ISO 3166-2:AD
u"AE",    #United Arab Emirates    1974    .ae ISO 3166-2:AE
u"AF",    #Afghanistan 1974    .af ISO 3166-2:AF
u"AG",    #Antigua and Barbuda 1974    .ag ISO 3166-2:AG
u"AI",    #Anguilla    1983    .ai ISO 3166-2:AI   AI previously represented French Afar and Issas
u"AL",    #Albania 1974    .al ISO 3166-2:AL
u"AM",    #Armenia 1992    .am ISO 3166-2:AM
u"AO",    #Angola  1974    .ao ISO 3166-2:AO
u"AQ",    #Antarctica  1974    .aq ISO 3166-2:AQ   Covers the territories south of 60o south latitude
       #Code taken from name in French: Antarctique
u"AR",    #Argentina   1974    .ar ISO 3166-2:AR
u"AS",    #American Samoa  1974    .as ISO 3166-2:AS
u"AT",    #Austria 1974    .at ISO 3166-2:AT
u"AU",    #Australia   1974    .au ISO 3166-2:AU   Includes the Ashmore and Cartier Islands and the Coral Sea Islands
u"AW",    #Aruba   1986    .aw ISO 3166-2:AW
u"AX",    #Åland Islands   2004    .ax ISO 3166-2:AX   An autonomous province of Finland
u"AZ",    #Azerbaijan  1992    .az ISO 3166-2:AZ
u"BA",    #Bosnia and Herzegovina  1992    .ba ISO 3166-2:BA
u"BB",    #Barbados    1974    .bb ISO 3166-2:BB
u"BD",    #Bangladesh  1974    .bd ISO 3166-2:BD
u"BE",    #Belgium 1974    .be ISO 3166-2:BE
u"BF",    #Burkina Faso    1984    .bf ISO 3166-2:BF   Name changed from Upper Volta (HV)
u"BG",    #Bulgaria    1974    .bg ISO 3166-2:BG
u"BH",    #Bahrain 1974    .bh ISO 3166-2:BH
u"BI",    #Burundi 1974    .bi ISO 3166-2:BI
u"BJ",    #Benin   1977    .bj ISO 3166-2:BJ   Name changed from Dahomey (DY)
u"BL",    #Saint Barthélemy    2007    .bl ISO 3166-2:BL
u"BM",    #Bermuda 1974    .bm ISO 3166-2:BM
u"BN",    #Brunei Darussalam   1974    .bn ISO 3166-2:BN   ISO country name follows UN designation (common name: Brunei)
u"BO",    #Bolivia, Plurinational State of 1974    .bo ISO 3166-2:BO   ISO country name follows UN designation (common name and previous ISO country name: Bolivia)
u"BQ",    #Bonaire, Sint Eustatius and Saba    2010    .bq ISO 3166-2:BQ   Consists of three Caribbean "special municipalities", which are part of the Netherlands proper: Bonaire, Sint Eustatius, and Saba (the BES Islands)
       #Previous ISO country name: Bonaire, Saint Eustatius and Saba
       #BQ previously represented British Antarctic Territory
u"BR",    #Brazil  1974    .br ISO 3166-2:BR
u"BS",    #Bahamas 1974    .bs ISO 3166-2:BS
u"BT",    #Bhutan  1974    .bt ISO 3166-2:BT
u"BV",    #Bouvet Island   1974    .bv ISO 3166-2:BV   Belongs to Norway
u"BW",    #Botswana    1974    .bw ISO 3166-2:BW
u"BY",    #Belarus 1974    .by ISO 3166-2:BY   Code taken from previous ISO country name: Byelorussian SSR (now assigned ISO 3166-3 code BYAA)
       #Code assigned as the country was already a UN member since 1945[17]
u"BZ",    #Belize  1974    .bz ISO 3166-2:BZ
u"CA",    #Canada  1974    .ca ISO 3166-2:CA
u"CC",    #Cocos (Keeling) Islands 1974    .cc ISO 3166-2:CC
u"CD",    #Congo, the Democratic Republic of the   1997    .cd ISO 3166-2:CD   Name changed from Zaire (ZR)
u"CF",    #Central African Republic    1974    .cf ISO 3166-2:CF
u"CG",    #Congo   1974    .cg ISO 3166-2:CG
u"CH",    #Switzerland 1974    .ch ISO 3166-2:CH   Code taken from name in Latin: Confoederatio Helvetica
u"CI",    #Côte d'Ivoire   1974    .ci ISO 3166-2:CI
u"CK",    #Cook Islands    1974    .ck ISO 3166-2:CK
u"CL",    #Chile   1974    .cl ISO 3166-2:CL
u"CM",    #Cameroon    1974    .cm ISO 3166-2:CM
u"CN",    #China   1974    .cn ISO 3166-2:CN
u"CO",    #Colombia    1974    .co ISO 3166-2:CO
u"CR",    #Costa Rica  1974    .cr ISO 3166-2:CR
u"CU",    #Cuba    1974    .cu ISO 3166-2:CU
u"CV",    #Cape Verde  1974    .cv ISO 3166-2:CV
u"CW",    #Curaçao 2010    .cw ISO 3166-2:CW
u"CX",    #Christmas Island    1974    .cx ISO 3166-2:CX
u"CY",    #Cyprus  1974    .cy ISO 3166-2:CY
u"CZ",    #Czech Republic  1993    .cz ISO 3166-2:CZ
u"DE",    #Germany 1974    .de ISO 3166-2:DE   Code taken from name in German: Deutschland
       #Code used for West Germany before 1990 (previous ISO country name: Germany, Federal Republic of)
u"DJ",    #Djibouti    1977    .dj ISO 3166-2:DJ   Name changed from French Afar and Issas (AI)
u"DK",    #Denmark 1974    .dk ISO 3166-2:DK
u"DM",    #Dominica    1974    .dm ISO 3166-2:DM
u"DO",    #Dominican Republic  1974    .do ISO 3166-2:DO
u"DZ",    #Algeria 1974    .dz ISO 3166-2:DZ   Code taken from name in Kabyle: Dzayer
u"EC",    #Ecuador 1974    .ec ISO 3166-2:EC
u"EE",    #Estonia 1992    .ee ISO 3166-2:EE   Code taken from name in Estonian: Eesti
u"EG",    #Egypt   1974    .eg ISO 3166-2:EG
u"EH",    #Western Sahara  1974    .eh ISO 3166-2:EH   Previous ISO country name: Spanish Sahara (code taken from name in Spanish: Sahara español)
u"ER",    #Eritrea 1993    .er ISO 3166-2:ER
u"ES",    #Spain   1974    .es ISO 3166-2:ES   Code taken from name in Spanish: España
u"ET",    #Ethiopia    1974    .et ISO 3166-2:ET
u"FI",    #Finland 1974    .fi ISO 3166-2:FI
u"FJ",    #Fiji    1974    .fj ISO 3166-2:FJ
u"FK",    #Falkland Islands (Malvinas) 1974    .fk ISO 3166-2:FK
u"FM",    #Micronesia, Federated States of 1986    .fm ISO 3166-2:FM   Previous ISO country name: Micronesia
u"FO",    #Faroe Islands   1974    .fo ISO 3166-2:FO
u"FR",    #France  1974    .fr ISO 3166-2:FR   Includes Clipperton Island
u"GA",    #Gabon   1974    .ga ISO 3166-2:GA
u"GB",    #United Kingdom  1974    .gb
       #(.uk)   ISO 3166-2:GB   Code taken from Great Britain (from official name: United Kingdom of Great Britain and Northern Ireland)[18]
       #.uk is the primary ccTLD of the United Kingdom instead of .gb (see code UK, which is exceptionally reserved)
u"GD",    #Grenada 1974    .gd ISO 3166-2:GD
u"GE",    #Georgia 1992    .ge ISO 3166-2:GE   GE previously represented Gilbert and Ellice Islands
u"GF",    #French Guiana   1974    .gf ISO 3166-2:GF   Code taken from name in French: Guyane française
u"GG",    #Guernsey    2006    .gg ISO 3166-2:GG   a British Crown dependency
u"GH",    #Ghana   1974    .gh ISO 3166-2:GH
u"GI",    #Gibraltar   1974    .gi ISO 3166-2:GI
u"GL",    #Greenland   1974    .gl ISO 3166-2:GL
u"GM",    #Gambia  1974    .gm ISO 3166-2:GM
u"GN",    #Guinea  1974    .gn ISO 3166-2:GN
u"GP",    #Guadeloupe  1974    .gp ISO 3166-2:GP
u"GQ",    #Equatorial Guinea   1974    .gq ISO 3166-2:GQ   Code taken from name in French: Guinée équatoriale
u"GR",    #Greece  1974    .gr ISO 3166-2:GR
u"GS",    #South Georgia and the South Sandwich Islands    1993    .gs ISO 3166-2:GS
u"GT",    #Guatemala   1974    .gt ISO 3166-2:GT
u"GU",    #Guam    1974    .gu ISO 3166-2:GU
u"GW",    #Guinea-Bissau   1974    .gw ISO 3166-2:GW
u"GY",    #Guyana  1974    .gy ISO 3166-2:GY
u"HK",    #Hong Kong   1974    .hk ISO 3166-2:HK
u"HM",    #Heard Island and McDonald Islands   1974    .hm ISO 3166-2:HM
u"HN",    #Honduras    1974    .hn ISO 3166-2:HN
u"HR",    #Croatia 1992    .hr ISO 3166-2:HR   Code taken from name in Croatian: Hrvatska
u"HT",    #Haiti   1974    .ht ISO 3166-2:HT
u"HU",    #Hungary 1974    .hu ISO 3166-2:HU
u"ID",    #Indonesia   1974    .id ISO 3166-2:ID
u"IE",    #Ireland 1974    .ie ISO 3166-2:IE
u"IL",    #Israel  1974    .il ISO 3166-2:IL
u"IM",    #Isle of Man 2006    .im ISO 3166-2:IM   a British Crown dependency
u"IN",    #India   1974    .in ISO 3166-2:IN
u"IO",    #British Indian Ocean Territory  1974    .io ISO 3166-2:IO
u"IQ",    #Iraq    1974    .iq ISO 3166-2:IQ
u"IR",    #Iran, Islamic Republic of   1974    .ir ISO 3166-2:IR   ISO country name follows UN designation (common name: Iran)
u"IS",    #Iceland 1974    .is ISO 3166-2:IS   Code taken from name in Icelandic: Ísland
u"IT",    #Italy   1974    .it ISO 3166-2:IT
u"JE",    #Jersey  2006    .je ISO 3166-2:JE   a British Crown dependency
u"JM",    #Jamaica 1974    .jm ISO 3166-2:JM
u"JO",    #Jordan  1974    .jo ISO 3166-2:JO
u"JP",    #Japan   1974    .jp ISO 3166-2:JP
u"KE",    #Kenya   1974    .ke ISO 3166-2:KE
u"KG",    #Kyrgyzstan  1992    .kg ISO 3166-2:KG
u"KH",    #Cambodia    1974    .kh ISO 3166-2:KH   Code taken from former name: Khmer Republic
       #Previous ISO country name: Kampuchea
u"KI",    #Kiribati    1979    .ki ISO 3166-2:KI
u"KM",    #Comoros 1974    .km ISO 3166-2:KM   Code taken from name in Comorian: Komori
u"KN",    #Saint Kitts and Nevis   1974    .kn ISO 3166-2:KN   Previous ISO country name: Saint Kitts-Nevis-Anguilla
u"KP",    #Korea, Democratic People's Republic of  1974    .kp ISO 3166-2:KP   ISO country name follows UN designation (common name: North Korea)
u"KR",    #Korea, Republic of  1974    .kr ISO 3166-2:KR   ISO country name follows UN designation (common name: South Korea)
u"KW",    #Kuwait  1974    .kw ISO 3166-2:KW
u"KY",    #Cayman Islands  1974    .ky ISO 3166-2:KY
u"KZ",    #Kazakhstan  1992    .kz ISO 3166-2:KZ   Previous ISO country name: Kazakstan
u"LA",    #Lao People's Democratic Republic    1974    .la ISO 3166-2:LA   ISO country name follows UN designation (common name: Laos)
u"LB",    #Lebanon 1974    .lb ISO 3166-2:LB
u"LC",    #Saint Lucia 1974    .lc ISO 3166-2:LC
u"LI",    #Liechtenstein   1974    .li ISO 3166-2:LI
u"LK",    #Sri Lanka   1974    .lk ISO 3166-2:LK
u"LR",    #Liberia 1974    .lr ISO 3166-2:LR
u"LS",    #Lesotho 1974    .ls ISO 3166-2:LS
u"LT",    #Lithuania   1992    .lt ISO 3166-2:LT
u"LU",    #Luxembourg  1974    .lu ISO 3166-2:LU
u"LV",    #Latvia  1992    .lv ISO 3166-2:LV
u"LY",    #Libya   1974    .ly ISO 3166-2:LY   Previous ISO country name: Libyan Arab Jamahiriya
u"MA",    #Morocco 1974    .ma ISO 3166-2:MA   Code taken from name in French: Maroc
u"MC",    #Monaco  1974    .mc ISO 3166-2:MC
u"MD",    #Moldova, Republic of    1992    .md ISO 3166-2:MD   ISO country name follows UN designation (common name and previous ISO country name: Moldova)
u"ME",    #Montenegro  2006    .me ISO 3166-2:ME
u"MF",    #Saint Martin (French part)  2007    .mf ISO 3166-2:MF   The Dutch part of Saint Martin island is assigned code SX
u"MG",    #Madagascar  1974    .mg ISO 3166-2:MG
u"MH",    #Marshall Islands    1986    .mh ISO 3166-2:MH
u"MK",    #Macedonia, the former Yugoslav Republic of  1993    .mk ISO 3166-2:MK   ISO country name follows UN designation (due to Macedonia naming dispute; official name used by country itself: Republic of Macedonia)
       #Code taken from name in Macedonian: Makedonija
u"ML",    #Mali    1974    .ml ISO 3166-2:ML
u"MM",    #Myanmar 1989    .mm ISO 3166-2:MM   Name changed from Burma (BU)
u"MN",    #Mongolia    1974    .mn ISO 3166-2:MN
u"MO",    #Macao   1974    .mo ISO 3166-2:MO   Previous ISO country name: Macau
u"MP",    #Northern Mariana Islands    1986    .mp ISO 3166-2:MP
u"MQ",    #Martinique  1974    .mq ISO 3166-2:MQ
u"MR",    #Mauritania  1974    .mr ISO 3166-2:MR
u"MS",    #Montserrat  1974    .ms ISO 3166-2:MS
u"MT",    #Malta   1974    .mt ISO 3166-2:MT
u"MU",    #Mauritius   1974    .mu ISO 3166-2:MU
u"MV",    #Maldives    1974    .mv ISO 3166-2:MV
u"MW",    #Malawi  1974    .mw ISO 3166-2:MW
u"MX",    #Mexico  1974    .mx ISO 3166-2:MX
u"MY",    #Malaysia    1974    .my ISO 3166-2:MY
u"MZ",    #Mozambique  1974    .mz ISO 3166-2:MZ
u"NA",    #Namibia 1974    .na ISO 3166-2:NA
u"NC",    #New Caledonia   1974    .nc ISO 3166-2:NC
u"NE",    #Niger   1974    .ne ISO 3166-2:NE
u"NF",    #Norfolk Island  1974    .nf ISO 3166-2:NF
u"NG",    #Nigeria 1974    .ng ISO 3166-2:NG
u"NI",    #Nicaragua   1974    .ni ISO 3166-2:NI
u"NL",    #Netherlands 1974    .nl ISO 3166-2:NL
u"NO",    #Norway  1974    .no ISO 3166-2:NO
u"NP",    #Nepal   1974    .np ISO 3166-2:NP
u"NR",    #Nauru   1974    .nr ISO 3166-2:NR
u"NU",    #Niue    1974    .nu ISO 3166-2:NU
u"NZ",    #New Zealand 1974    .nz ISO 3166-2:NZ
u"OM",    #Oman    1974    .om ISO 3166-2:OM
u"PA",    #Panama  1974    .pa ISO 3166-2:PA
u"PE",    #Peru    1974    .pe ISO 3166-2:PE
u"PF",    #French Polynesia    1974    .pf ISO 3166-2:PF   Code taken from name in French: Polynésie française
u"PG",    #Papua New Guinea    1974    .pg ISO 3166-2:PG
u"PH",    #Philippines 1974    .ph ISO 3166-2:PH
u"PK",    #Pakistan    1974    .pk ISO 3166-2:PK
u"PL",    #Poland  1974    .pl ISO 3166-2:PL
u"PM",    #Saint Pierre and Miquelon   1974    .pm ISO 3166-2:PM
u"PN",    #Pitcairn    1974    .pn ISO 3166-2:PN
u"PR",    #Puerto Rico 1974    .pr ISO 3166-2:PR
u"PS",    #Palestine, State of 1999    .ps ISO 3166-2:PS   Previous ISO country name: Palestinian Territory, Occupied
       #Consists of the West Bank and the Gaza Strip
u"PT",    #Portugal    1974    .pt ISO 3166-2:PT
u"PW",    #Palau   1986    .pw ISO 3166-2:PW
u"PY",    #Paraguay    1974    .py ISO 3166-2:PY
u"QA",    #Qatar   1974    .qa ISO 3166-2:QA
u"RE",    #Réunion 1974    .re ISO 3166-2:RE
u"RO",    #Romania 1974    .ro ISO 3166-2:RO
u"RS",    #Serbia  2006    .rs ISO 3166-2:RS   Code taken from official name: Republic of Serbia (see Serbian country codes)
u"RU",    #Russian Federation  1992    .ru ISO 3166-2:RU   ISO country name follows UN designation (common name: Russia)
u"RW",    #Rwanda  1974    .rw ISO 3166-2:RW
u"SA",    #Saudi Arabia    1974    .sa ISO 3166-2:SA
u"SB",    #Solomon Islands 1974    .sb ISO 3166-2:SB   Code taken from former name: British Solomon Islands
u"SC",    #Seychelles  1974    .sc ISO 3166-2:SC
u"SD",    #Sudan   1974    .sd ISO 3166-2:SD
u"SE",    #Sweden  1974    .se ISO 3166-2:SE
u"SG",    #Singapore   1974    .sg ISO 3166-2:SG
u"SH",    #Saint Helena, Ascension and Tristan da Cunha    1974    .sh ISO 3166-2:SH   Previous ISO country name: Saint Helena
u"SI",    #Slovenia    1992    .si ISO 3166-2:SI
u"SJ",    #Svalbard and Jan Mayen  1974    .sj ISO 3166-2:SJ   Consists of two arctic territories of Norway: Svalbard and Jan Mayen
u"SK",    #Slovakia    1993    .sk ISO 3166-2:SK   SK previously represented Sikkim
u"SL",    #Sierra Leone    1974    .sl ISO 3166-2:SL
u"SM",    #San Marino  1974    .sm ISO 3166-2:SM
u"SN",    #Senegal 1974    .sn ISO 3166-2:SN
u"SO",    #Somalia 1974    .so ISO 3166-2:SO
u"SR",    #Suriname    1974    .sr ISO 3166-2:SR
u"SS",    #South Sudan 2011    .ss ISO 3166-2:SS
u"ST",    #Sao Tome and Principe   1974    .st ISO 3166-2:ST
u"SV",    #El Salvador 1974    .sv ISO 3166-2:SV
u"SX",    #Sint Maarten (Dutch part)   2010    .sx ISO 3166-2:SX   The French part of Saint Martin island is assigned code MF
u"SY",    #Syrian Arab Republic    1974    .sy ISO 3166-2:SY   ISO country name follows UN designation (common name: Syria)
u"SZ",    #Swaziland   1974    .sz ISO 3166-2:SZ
u"TC",    #Turks and Caicos Islands    1974    .tc ISO 3166-2:TC
u"TD",    #Chad    1974    .td ISO 3166-2:TD   Code taken from name in French: Tchad
u"TF",    #French Southern Territories 1979    .tf ISO 3166-2:TF   Covers the French Southern and Antarctic Lands except Adélie Land
       #Code taken from name in French: Terres australes françaises
u"TG",    #Togo    1974    .tg ISO 3166-2:TG
u"TH",    #Thailand    1974    .th ISO 3166-2:TH
u"TJ",    #Tajikistan  1992    .tj ISO 3166-2:TJ
u"TK",    #Tokelau 1974    .tk ISO 3166-2:TK
u"TL",    #Timor-Leste 2002    .tl ISO 3166-2:TL   Name changed from East Timor (TP)
u"TM",    #Turkmenistan    1992    .tm ISO 3166-2:TM
u"TN",    #Tunisia 1974    .tn ISO 3166-2:TN
u"TO",    #Tonga   1974    .to ISO 3166-2:TO
u"TR",    #Turkey  1974    .tr ISO 3166-2:TR
u"TT",    #Trinidad and Tobago 1974    .tt ISO 3166-2:TT
u"TV",    #Tuvalu  1979    .tv ISO 3166-2:TV
u"TW",    #Taiwan, Province of China   1974    .tw ISO 3166-2:TW   Covers the current jurisdiction of the Republic of China except Kinmen and Lienchiang
       #ISO country name follows UN designation (due to political status of Taiwan within the UN)[18]
u"TZ",    #Tanzania, United Republic of    1974    .tz ISO 3166-2:TZ   ISO country name follows UN designation (common name: Tanzania)
u"UA",    #Ukraine 1974    .ua ISO 3166-2:UA   Previous ISO country name: Ukrainian SSR
       #Code assigned as the country was already a UN member since 1945[17]
u"UG",    #Uganda  1974    .ug ISO 3166-2:UG
u"UM",    #United States Minor Outlying Islands    1986    .um ISO 3166-2:UM   Consists of nine minor insular areas of the United States: Baker Island, Howland Island, Jarvis Island, Johnston Atoll, Kingman Reef, Midway Islands, Navassa Island, Palmyra Atoll, and Wake Island
u"US",    #United States   1974    .us ISO 3166-2:US
u"UY",    #Uruguay 1974    .uy ISO 3166-2:UY
u"UZ",    #Uzbekistan  1992    .uz ISO 3166-2:UZ
u"VA",    #Holy See (Vatican City State)   1974    .va ISO 3166-2:VA   Covers Vatican City, territory of the Holy See
       #Previous ISO country name: Vatican City State (Holy See)
u"VC",    #Saint Vincent and the Grenadines    1974    .vc ISO 3166-2:VC
u"VE",    #Venezuela, Bolivarian Republic of   1974    .ve ISO 3166-2:VE   ISO country name follows UN designation (common name and previous ISO country name: Venezuela)
u"VG",    #Virgin Islands, British 1974    .vg ISO 3166-2:VG
u"VI",    #Virgin Islands, U.S.    1974    .vi ISO 3166-2:VI
u"VN",    #Viet Nam    1974    .vn ISO 3166-2:VN   ISO country name follows UN designation (common name: Vietnam)
u"VU",    #Vanuatu 1980    .vu ISO 3166-2:VU   Name changed from New Hebrides (NH)
u"WF",    #Wallis and Futuna   1974    .wf ISO 3166-2:WF
u"WS",    #Samoa   1974    .ws ISO 3166-2:WS   Code taken from former name: Western Samoa
u"YE",    #Yemen   1974    .ye ISO 3166-2:YE   Previous ISO country name: Yemen, Republic of
       #Code used for North Yemen before 1990
u"YT",    #Mayotte 1993    .yt ISO 3166-2:YT
u"ZA",    #South Africa    1974    .za ISO 3166-2:ZA   Code taken from name in Dutch: Zuid-Afrika
u"ZM",    #Zambia  1974    .zm ISO 3166-2:ZM
u"ZW",    #Zimbabwe    1980    .zw ISO 3166-2:ZW   Name changed from Southern Rhodesia (RH)
]

ALLOWED_COUNTRY_CODES = COUNTRY_CODES + ["EU"]
KNOWN_COUNTRY_CODES = ALLOWED_COUNTRY_CODES
