
from flask import Flask, render_template_string

app = Flask(__name__)

QUESTIONS = [
    {"q":"Lưu vực sông Mekong trải dài qua bao nhiêu quốc gia?",
     "o":["4 quốc gia","5 quốc gia","6 quốc gia","7 quốc gia"],"a":2,
     "e":"Lưu vực Mekong trải qua Trung Quốc, Myanmar, Lào, Thái Lan, Campuchia và Việt Nam."},
    {"q":"Sông Mekong bắt nguồn từ khu vực nào?",
     "o":["Dãy núi Himalaya","Cao nguyên Thanh Tạng (Trung Quốc)","Dãy núi Trường Sơn","Cao nguyên Đê-can (Ấn Độ)"],"a":1,
     "e":"Sông Mekong bắt nguồn từ vùng núi cao thuộc cao nguyên Thanh Tạng ở Trung Quốc."},
    {"q":"Đặc điểm địa hình chủ yếu của khu vực thượng lưu sông Mekong là gì?",
     "o":["Đồng bằng thấp và bằng phẳng","Đồi cát và vùng ven biển","Núi cao, cao nguyên và thung lũng sâu","Đồng bằng châu thổ rộng lớn"],"a":2,
     "e":"Thượng lưu có địa hình núi cao, cao nguyên và thung lũng sâu; lòng sông có độ dốc lớn."},
    {"q":"Biển Hồ Tonlé Sap có vai trò chủ yếu nào đối với hệ thống sông Mekong?",
     "o":["Điều tiết dòng chảy theo mùa","Cung cấp nước biển cho lưu vực","Ngăn cản dòng sông chảy ra biển","Làm tăng độ mặn của nước sông"],"a":0,
     "e":"Biển Hồ Tonlé Sap trao đổi nước với sông Mekong theo mùa, góp phần điều hòa dòng chảy ở hạ lưu."},
    {"q":"Đâu là nhóm tài nguyên thiên nhiên tiêu biểu của lưu vực sông Mekong?",
     "o":["Dầu mỏ, khí tự nhiên và băng tuyết","Nước, đất phù sa, thủy sản và tiềm năng thủy điện","Khoáng sản kim loại quý và than đá","Cát sa mạc, muối và tài nguyên băng hà"],"a":1,
     "e":"Các tài nguyên tiêu biểu gồm nước, đất phù sa, sinh vật – thủy sản và tiềm năng thủy điện."}
]

HTML = r"""<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Giải mã sông Mekong</title>
<style>
*{box-sizing:border-box}body{margin:0;padding:26px 15px;background:linear-gradient(135deg,#e7f4f0,#f3f7fa);font-family:Arial,sans-serif;color:#17313b}
.wrap{max-width:820px;margin:auto}.hero{background:linear-gradient(120deg,#103b4b,#147d76);color:white;text-align:center;padding:32px 20px;border-radius:20px}
h1{margin:9px 0;font-size:clamp(27px,5vw,40px)}.hero p{line-height:1.5}.pills{display:flex;justify-content:center;gap:8px;flex-wrap:wrap}.pill{border:1px solid #ffffff66;border-radius:30px;padding:7px 12px;font-size:13px}
.card{background:white;margin-top:18px;padding:24px;border:1px solid #dce7e8;border-radius:18px;box-shadow:0 8px 24px #163b4a0d}
.top{display:flex;justify-content:space-between;gap:10px;color:#167d75;font-weight:bold}.muted{color:#647780;font-weight:normal}
.track{height:8px;background:#e8eeee;border-radius:20px;margin:15px 0 24px;overflow:hidden}.bar{height:100%;width:0;background:#168b7e;transition:.2s}
h2{font-size:21px;line-height:1.4}.choices{display:grid;gap:10px}
.choice{display:flex;align-items:center;gap:12px;width:100%;padding:13px;text-align:left;background:white;border:1.5px solid #dce7e8;border-radius:12px;font-size:15px;cursor:pointer;color:#17313b}
.choice:hover:not(:disabled){border-color:#167d75;background:#f4fbf9}.choice:disabled{cursor:default;opacity:1}
.letter{flex:0 0 32px;height:32px;display:grid;place-items:center;border-radius:9px;background:#edf4f4;font-weight:bold}
.correct{background:#eaf7ef!important;border-color:#16834a!important}.correct .letter{background:#16834a;color:white}
.wrong{background:#fff0ef!important;border-color:#c44747!important}.wrong .letter{background:#c44747;color:white}
.feedback{display:none;padding:14px;margin-top:15px;border-radius:12px;line-height:1.5}.feedback.show{display:block}.good{background:#eaf7ef;color:#145d37}.bad{background:#fff0ef;color:#873333}
button.next{display:block;margin:18px 0 0 auto;background:#12394a;color:white;border:0;padding:13px 20px;border-radius:11px;font-weight:bold;cursor:pointer}button:disabled{opacity:.45;cursor:not-allowed}
.result{display:none;text-align:center}.result.show{display:block}.points{font-size:42px;color:#167d75;font-weight:bold}.review{text-align:left;line-height:1.6;margin-top:20px}.review div{padding:9px 0;border-bottom:1px solid #e1e9e9}
footer{text-align:center;color:#647780;font-size:13px;margin:18px}
@media(max-width:500px){.card{padding:17px}.choice{font-size:14px}h2{font-size:19px}}
</style></head><body><div class="wrap">
<header class="hero"><div>THỬ THÁCH KIẾN THỨC ĐỊA LÍ 11</div><h1>GIẢI MÃ SÔNG MEKONG</h1>
<p>Chinh phục 5 câu hỏi về đặc điểm tự nhiên và tài nguyên của lưu vực sông Mekong.</p>
<div class="pills"><span class="pill">5 câu hỏi</span><span class="pill">10 điểm / câu</span><span class="pill">Tối đa 50 điểm</span></div></header>
<main class="card" id="quiz"><div class="top"><span id="counter">CÂU 1 / 5</span><span class="muted" id="score">Điểm: 0 / 50</span></div>
<div class="track"><div class="bar" id="bar"></div></div><h2 id="question"></h2><div class="choices" id="choices"></div>
<div id="feedback" class="feedback" aria-live="polite"></div><button class="next" id="next" disabled>Câu tiếp theo →</button></main>
<section class="card result" id="result"><div style="font-size:48px">🏆</div><h2>HOÀN THÀNH THỬ THÁCH!</h2>
<div class="points" id="final"></div><p id="message"></p><div class="review" id="review"></div>
<button class="next" onclick="restart()">Chơi lại ↻</button></section>
<footer>Trò chơi ôn tập: Tổng quan về đặc điểm tự nhiên lưu vực sông Mekong</footer></div>
<script>
const questions=__QUESTIONS__;
let current=0,score=0,selected=null,history=[];
const letters=["A","B","C","D"];
const $=id=>document.getElementById(id);
function render(){
 selected=null;const q=questions[current];
 $("counter").textContent=`CÂU ${current+1} / ${questions.length}`;
 $("score").textContent=`Điểm: ${score} / 50`;
 $("bar").style.width=`${current/questions.length*100}%`;
 $("question").textContent=q.q;$("choices").innerHTML="";
 $("feedback").className="feedback";$("feedback").textContent="";
 $("next").disabled=true;$("next").textContent=current===4?"Xem kết quả →":"Câu tiếp theo →";
 q.o.forEach((v,i)=>{const b=document.createElement("button");b.className="choice";
 const l=document.createElement("span");l.className="letter";l.textContent=letters[i];
 const t=document.createElement("span");t.textContent=v;b.append(l,t);b.onclick=()=>answer(i);$("choices").append(b)});
}
function answer(i){
 if(selected!==null)return;selected=i;const q=questions[current],ok=i===q.a;
 if(ok)score+=10;history.push({chosen:i,ok});
 [...$("choices").children].forEach((b,n)=>{b.disabled=true;if(n===q.a)b.classList.add("correct");if(n===i&&!ok)b.classList.add("wrong")});
 const f=$("feedback");f.className="feedback show "+(ok?"good":"bad");
 f.textContent=(ok?"✓ Chính xác! Bạn được cộng 10 điểm. ":"✗ Chưa chính xác! Đáp án đúng: "+letters[q.a]+". "+q.o[q.a]+". ")+q.e;
 $("score").textContent=`Điểm: ${score} / 50`;$("next").disabled=false;
}
$("next").onclick=()=>{if(selected===null)return;if(current<4){current++;render()}else finish()};
function finish(){
 $("quiz").style.display="none";$("result").classList.add("show");$("bar").style.width="100%";
 $("final").textContent=score+" / 50 điểm";
 $("message").textContent=score===50?"Xuất sắc! Bạn đã chinh phục trọn vẹn thử thách Mekong.":score>=30?"Khá tốt! Bạn đã nắm được nhiều kiến thức quan trọng.":"Hãy xem lại phần giải thích và thử sức thêm lần nữa nhé.";
 $("review").innerHTML="<strong>Kết quả từng câu</strong>";
 questions.forEach((q,i)=>{const d=document.createElement("div");d.textContent=`Câu ${i+1}: ${history[i].ok?"✓ Đúng":"✗ Sai"} — Đáp án ${letters[q.a]}. ${q.o[q.a]}`;$("review").append(d)});
}
function restart(){current=0;score=0;selected=null;history=[];$("quiz").style.display="block";$("result").classList.remove("show");render()}
render();
</script></body></html>"""

@app.route("/")
def home():
    import json
    return render_template_string(HTML.replace("__QUESTIONS__", json.dumps(QUESTIONS, ensure_ascii=False)))

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
