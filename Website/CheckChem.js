Date = "1/10/2022";
DayofWeek = 0;
CL = [];
ORP = []; 
PH = []; 
TA = []; 
FLOW = []; 
TEMP = []; 
INITIALS = []; 
RadioValue = 3; 
function Setup() {
    eel.SetupChem(); 
}
function RunChem()  {
    Submit(); 
    TDate = document.getElementById("Date").value; 
    if(RadioValue == 3) {
        console.log("select lap or act"); 
    } else {
        eel.ChemCheck(CL, ORP, PH,TA,FLOW,TEMP,INITIALS, TDate, RadioValue);
    }
    
}
function ClickLap() {
    console.log(document.getElementById("Actinput").value)
    
}
function ClickAct() {

}
categories = ["CL", "ORP", "PH","TA","FLOW","TEMP","INITIALS"]; 
function Submit() {
    for(let x = 0; x<7; x++){
        eval(categories[x]).length = 0; 
         
    }
    for(let y = 0; y< 7; y++) {
        var Cat = categories[y]
        for(let x =0; x< 6; x++) {
            if(document.getElementById(Cat + String(x+1)).value == "") {
                if(Cat == "INITIALS") {
                    eval(Cat).push("n/a"); 
                } else {
                    eval(Cat).push(0); 
                }
            } else {
                eval(Cat).push(document.getElementById(Cat + String(x+1)).value); 
            }
        }
        console.log(eval(Cat)); 
        console.log(Cat); 
    }
    
}
function SelLap() {
    RadioValue =0
}
function SelAct() {
    RadioValue =1 
}