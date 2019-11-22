from flask import Blueprint, request

bp = Blueprint('textcompare_bp',__name__)

@bp.route("/",methods=["POST"])
def compare_text():

    lcs=[]
    
    data = request.json

    txt2 = data["text2"]
    txt1 = data["text1"]

    text1 = ("@ " + txt1).split(" ")
    text2 = ("@ " + txt2).split(" ")

    total_len = max(len(text1), len(text2))
   
    text1_l = len(text1)
    text2_l = len(text2)
   
    for indx1 in range(0, text1_l):
        row=[]
        
        for indx2 in range(0, text2_l):
            
            if indx1 == 0 or indx2 == 0:
                row.insert(indx2,0)
            elif text1[indx1] == text2[indx2]:
                
                row.insert(indx2,lcs[indx1 - 1][indx2 - 1] + 1)
            else:
                row.insert(indx2,max(row[indx2 - 1], lcs[indx1 - 1][indx2]))
        
        lcs.insert(indx1 + 1,row)

    sub_seq = lcs[text1_l - 1][text2_l - 1]

    msg = dict(Match_count=sub_seq,
               Match_Score=sub_seq/(total_len - 1)
               )

    return msg , 201




                    





    

