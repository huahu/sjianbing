function ExChgClsName(Obj,NameA,NameB){
  var Obj=document.getElementById(Obj)?document.getElementById(Obj):Obj;
  Obj.className=Obj.className==NameA?NameB:NameA;
 }

function showmenu_zzjs(iNo){
 ExChgClsName("zzjs_"+iNo,"menu_zzjs_1","menu_zzjs_2");
 }

function switchbox(i)
{
 selectbox(i);
}
function selectbox(i)
{
 switch(i)
 {
 case 1:
 document.getElementById("red").style.display="block";
 document.getElementById("green").style.display="none";
 document.getElementById("blue").style.display="none";
 break;
 case 2:
 document.getElementById("red").style.display="none";
 document.getElementById("green").style.display="block";
 document.getElementById("blue").style.display="none";
 break;
 case 3:
 document.getElementById("red").style.display="none";
 document.getElementById("green").style.display="none";
 document.getElementById("blue").style.display="block";
 break;
 }
}

function getSelectValue(){
    var oSelect = document.getElementById("select");
  	var oShow = document.getElementById("show");
  	oShow.value = oSelect.options[oSelect.selectedIndex].value;
}
