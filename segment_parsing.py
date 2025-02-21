import regex as re

letter = r"("+r"|".join(list(r"QWERTYUIOPASDFGHJKLZXCVBNMäãẽĩõũỹǎěǐǒǔâêîôûàèìòùáéíóúqwertyuiopasdfhjklzxcvbnmɑæɐɑβɓʙçɕðɖɗəɚɵɘɛɜɝɞɠɢʛɡħɦɥɧʜɪɨʝɟʄɫɭɬʟɮɱŋɲɳɴɔœɒɶøɸɾɹʁʀɻɽɺʃʂθʈʊʉʌʋⱱɯʍɰχɣʎʏɤʒʐʑʔʕʡʢʘǀǁǂǃ˩˨˧˦˥"))+r")"
post_diacritic = r"("+r"|".join(list(r"ː̆ʰʲʷ̩̯̥̬̪̺̝̞̟̠̃̈̚ˑˤᵝʱˡˠʼ̹̜̤̰̼̘̙̻˞̑̊̽ꜜꜛ̏̀̄́̋̂̌᷅᷄᷈ꜜꜛ"))+r")"
pre_diacritic = r"(ˈ|ˌ|ˀ|ⁿ|ᵐ|ᶯ|ᶮ|ᵑ|ᶰ)"


##########################################################################################################
# Takes a string as an argument and returns the same string stripped off of spaces, new-line characters, #
# and the following non-IPA symbols:                                                                     #
# . ~ < > = - ‖ | [ ] / ( ) ,                                                                            #
#                                                                                                        #
# It also substitutes non-IPA 'g' with IPA 'ɡ'.                                                          #
##########################################################################################################
def clean(segment_string):
    cleaned_segment_string = segment_string
    cleaned_segment_string = re.sub(r"(\.|~|<|>|=|-| |‖|\||\n|\[|\]|\/|\(|\)|,)", "", cleaned_segment_string)
    cleaned_segment_string = cleaned_segment_string.replace("g", "ɡ")
    return cleaned_segment_string


##########################################################################################################
# Takes a string as an argument and returns a list of its segments.                                      #
##########################################################################################################
def parse_segments_of(segment_string):
    segment_list = segment_string
    pns = [
            re.compile(pre_diacritic + r"*" + letter + post_diacritic + r"*(͡|͜)" + letter + post_diacritic + r"*"),
            re.compile(r"(?<=([^͜͡]|\b))" + pre_diacritic + r"*" + letter + post_diacritic + r"*(?=([^͜͡]|\b))")
          ]
    
    for pn in pns:
        segment_list = pn.sub(r" \g<0>", segment_list)
    
    segment_list = segment_list.strip(" ").split(" ")
    return segment_list