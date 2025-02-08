import numpy as np
from itertools import combinations

#Given 5 phrases and their embeddings as an array
embeddings = {
    "I love the variety of products available.":[0.1263255476951599,-0.3116876780986786,-0.1845686137676239,0.14346520602703094,0.025372233241796494,-0.2828041911125183,0.09950517863035202,0.23424185812473297,-0.03733427822589874,0.0246580820530653,0.15838304162025452,-0.19409063458442688,-0.16615936160087585,0.07708873599767685,0.03473556041717529,-0.08458733558654785,-0.18012499809265137,0.1893296241760254,-0.09109405428171158,0.08065950125455856,0.08831679821014404,0.04641987755894661,-0.13743458688259125,-0.18075980246067047,-0.01637590117752552,-0.14092598855495453,-0.23630495369434357,0.06447205692529678,0.07486693561077118,-0.08181007951498032,0.06530523300170898,-0.21678480505943298,-0.06542425602674484,0.021603098139166832,0.005911591462790966,0.1277538537979126,-0.004547759424895048,0.05074446648359299,0.32470110058784485,-0.08546018600463867,-0.04284911975264549,0.07546205818653107,0.202660471200943,-0.08553953468799591,0.00024378496163990349,-0.03582662343978882,-0.29058051109313965,-0.08950705081224442,0.03743346780538559,-0.06633678823709488],
    "Product arrived on time and in perfect condition.":[-0.010682418942451477,0.11619731038808823,-0.42015066742897034,0.1391039341688156,0.20674702525138855,-0.09710845351219177,-0.04236258193850517,0.0037688259035348892,-0.05031627416610718,0.06563630700111389,0.005188253708183765,-0.030786903575062752,-0.17532382905483246,-0.2596084773540497,0.08276733756065369,0.01502635795623064,-0.004181805998086929,-0.15662653744220734,-0.08702562004327774,0.18550455570220947,0.02115681767463684,-0.007965927943587303,0.13039158284664154,-0.14341117441654205,-0.05310618504881859,-0.12814007699489594,0.1322515308856964,-0.057853925973176956,0.08506778627634048,-0.20635545253753662,0.19088858366012573,-0.11414158344268799,0.16064009070396423,0.041946545243263245,0.09099023044109344,0.08692772686481476,0.238463893532753,0.12569279968738556,-0.04882342740893364,0.10131778568029404,-0.28251510858535767,-0.028902489691972733,0.08012425899505615,0.22045184671878815,-0.21868979930877686,0.006102928426116705,-0.2081174999475479,0.10464610159397125,-0.005332032218575478,0.11394580453634262],
    "There was a delay in delivery.":[0.14162038266658783,0.133348748087883,-0.04399004951119423,-0.10571397840976715,-0.12250789999961853,0.039634909480810165,0.010010556317865849,0.028512069955468178,-0.011859141290187836,-0.11755745112895966,-0.011624150909483433,-0.05646016448736191,-0.07576064020395279,-0.26845210790634155,-0.060000672936439514,-0.07820453494787216,0.04865850880742073,-0.1497666984796524,-0.28549668192863464,0.24902629852294922,0.0857868641614914,0.053608957678079605,0.24727170169353485,0.0352797694504261,-0.16643528640270233,-0.060595981776714325,0.1174321249127388,-0.17596019804477692,0.04847051948308945,0.14939071238040924,0.12282121926546097,-0.10019955784082413,0.23448826372623444,-0.22408606112003326,-0.16217415034770966,0.1520226001739502,-0.0021325305569916964,0.19927117228507996,0.15578243136405945,0.1492653787136078,-0.26845210790634155,-0.1048993468284607,-0.11906138807535172,-0.012994923628866673,-0.07444469630718231,0.22797122597694397,-0.05166637524962425,-0.07469535619020462,-0.009728568606078625,0.23611752688884735],
    "Customer support was unresponsive.":[-0.06957648694515228,0.06539750099182129,-0.10396149754524231,-0.018622158095240593,-0.18270243704319,-0.20059143006801605,-0.05971554294228554,0.19472618401050568,0.20792299509048462,-0.03706102818250656,0.06796354800462723,-0.15616218745708466,-0.09516362845897675,-0.1022019237279892,-0.12558959424495697,0.12163054943084717,0.03737261891365051,-0.008871185593307018,-0.3882793188095093,0.06330800801515579,0.1365136206150055,0.15792176127433777,0.1545492559671402,-0.10506123304367065,-0.20132459700107574,0.21100224554538727,0.07041961699724197,-0.02917960286140442,-0.11019331961870193,-0.039663732051849365,0.26408272981643677,-0.236516073346138,0.11239279061555862,-0.005429935175925493,-0.1417190283536911,0.08511938899755478,0.0920843705534935,0.15880155563354492,0.13050173223018646,0.2516190707683563,-0.07423202693462372,-0.022013003006577492,0.07265574485063553,0.10880032926797867,-0.19194020330905914,0.16452017426490784,-0.049561332911252975,0.151616632938385,-0.07991398870944977,0.05535326525568962],
    "Fast shipping and great service.":[-0.1079404279589653,0.020684150978922844,-0.30074435472488403,0.11729881167411804,0.13952496647834778,-0.018052106723189354,-0.21843314170837402,0.13527116179466248,-0.09257353842258453,-0.09384968131780624,0.11293865740299225,-0.03900212049484253,-0.059287477284669876,-0.1008152961730957,-0.019155437126755714,-0.007078605704009533,-0.02967032417654991,0.03711449354887009,-0.18302017450332642,0.20056714117527008,0.09076566994190216,0.02584189549088478,0.0943814069032669,-0.03799184039235115,-0.25246360898017883,-0.1235731765627861,0.028952494263648987,-0.309251993894577,0.021375395357608795,-0.22204887866973877,0.2159872055053711,-0.11921302229166031,0.21928390860557556,-0.11432114243507385,0.017453914508223534,0.10065577924251556,-0.04200637340545654,0.17493793368339539,0.1322934925556183,0.17025874555110931,-0.15271177887916565,0.004682514350861311,0.2531017065048218,0.11580997705459595,0.014688937924802303,-0.11176885664463043,-0.292662113904953,-0.0397731214761734,0.13729171454906464,0.027570005506277084]
    }

def cosine_similarity(vector1, vector2):
    #Cosine similarity between the two texts
    vector1, vector2 = np.array(vector1), np.array(vector2)  # Ensure they are NumPy arrays
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))

def most_similar_finding(embeddings):
    #Function to find the 2 most closest phrases having smallest cosine angle out of 5 phrases
    #max_similarity = -float("inf")
    max_similarity = -1

    for (phrase_one, emb_one), (phrase_two, emb_two) in combinations(embeddings.items(), 2):
        similarity = cosine_similarity(emb_one, emb_two)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_pair = (phrase_one, phrase_two)

    return most_similar_pair

print("Most similar two feedback phrases:", most_similar_finding(embeddings))