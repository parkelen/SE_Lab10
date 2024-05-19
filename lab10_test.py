from lab10 import getinfo
def test_1():
    line = ['11,1,3,"Sandstrom, Miss. Marguerite Rut",female,4,1,1,PP 9549,16.7,G6,S',
            '12,1,1,"Bonnell, Miss. Elizabeth",female,58,0,0,113783,26.55,C103,S',
            '13,0,3,"Saundercock, Mr. William Henry",male,20,0,0,A/5. 2151,8.05,,S',
            '14,0,3,"Andersson, Mr. Anders Johan",male,39,1,5,347082,31.275,,S',
            '15,0,3,"Vestrom, Miss. Hulda Amanda Adolfina",female,14,0,0,350406,7.8542,,S',
            '16,1,2,"Hewlett, Mrs. (Mary D Kingcome) ",female,55,0,0,248706,16,,S',
            '17,0,3,"Rice, Master. Eugene",male,2,4,1,382652,29.125,,Q',
            '18,1,2,"Williams, Mr. Charles Eugene",male,,0,0,244373,13,,S',
            '19,0,3,"Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)",female,31,1,0,345763,18,,S',
            '20,1,3,"Masselmani, Mrs. Fatima",female,,0,0,2649,7.225,,C',
            '21,0,2,"Fynney, Mr. Joseph J",male,35,0,0,239865,26,,S',
            '22,1,2,"Beesley, Mr. Lawrence",male,34,0,0,248698,13,D56,S',
            '23,1,3,"McGowan, Miss. Anna ""Annie""",female,15,0,0,330923,8.0292,,Q']
    actual = getinfo(line,"0")
    expected = (40.0, 71.42857142857143)
    print(actual)
    assert actual == expected
def test_2():
    line = ['11,1,3,"Sandstrom, Miss. Marguerite Rut",female,4,1,1,PP 9549,16.7,G6,S',
            '12,1,1,"Bonnell, Miss. Elizabeth",female,58,0,0,113783,26.55,C103,S',
            '13,0,3,"Saundercock, Mr. William Henry",male,20,0,0,A/5. 2151,8.05,,S',
            '14,0,3,"Andersson, Mr. Anders Johan",male,39,1,5,347082,31.275,,S',
            '15,0,3,"Vestrom, Miss. Hulda Amanda Adolfina",female,14,0,0,350406,7.8542,,S',
            '16,1,2,"Hewlett, Mrs. (Mary D Kingcome) ",female,55,0,0,248706,16,,S',
            '17,0,3,"Rice, Master. Eugene",male,2,4,1,382652,29.125,,Q',
            '18,1,2,"Williams, Mr. Charles Eugene",male,,0,0,244373,13,,S',
            '19,0,3,"Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)",female,31,1,0,345763,18,,S',
            '20,1,3,"Masselmani, Mrs. Fatima",female,,0,0,2649,7.225,,C',
            '21,0,2,"Fynney, Mr. Joseph J",male,35,0,0,239865,26,,S',
            '22,1,2,"Beesley, Mr. Lawrence",male,34,0,0,248698,13,D56,S',
            '23,1,3,"McGowan, Miss. Anna ""Annie""",female,15,0,0,330923,8.0292,,Q']
    actual = getinfo(line,"1-2")
    expected = (0.0, 50.0)
    print(actual)
    assert actual == expected
def test_3():
    line =['19,0,3,"Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)",female,31,1,0,345763,18,,S',
            '20,1,3,"Masselmani, Mrs. Fatima",female,,0,0,2649,7.225,,C',
            '21,0,2,"Fynney, Mr. Joseph J",male,35,0,0,239865,26,,S',
            '22,1,2,"Beesley, Mr. Lawrence",male,34,0,0,248698,13,D56,S',]
    actual = getinfo(line,"Больше 2")
    expected = (50.0, 50.0)
    print(actual)
    assert actual == expected