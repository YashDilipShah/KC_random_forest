function vaidate()
{
	var flag=document.getElementByclass('block1');
	var check1=document.getElementById('yo1');
	var check2=document.getElementById('yo2');
	var check3=document.getElementById('yo3');
	var check4=document.getElementById('yo4');
	var check5=document.getElementById('yo5');
	var check6=document.getElementById('yo6');
	var check7=document.getElementById('yo7');
	var check8=document.getElementById('yo8');
	var check9=document.getElementById('yo9');
	var check10=document.getElementById('yo10');
	var check11=document.getElementById('yo11');
	var check12=document.getElementById('yo12');
	var check13=document.getElementById('yo13');
	/*var check14=document.getElementById('yo14');
	var check15=document.getElementById('yo15');*/
	if(check1.value.trim()==""||check2.value.trim()==""||check3.value.trim()==""||check4.value.trim()==""||check5.value.trim()==""||check6.value.trim()==""||check7.value.trim()==""||check8.value.trim()==""||check9.value.trim()==""||check10.value.trim()==""||check11.value.trim()==""||check12.value.trim()==""||check13.value.trim()=="")
	{
		alert("Please fill all the details");
		return false;
	}
	else if(typeof(flag)!=number)
	{
		alert("Please enter an non-negative integer value");
		return false;
	}
	else{
		return true;
	}
}
function required(inputtx)
{
	if(inputtx.value.length==0){
		alert("please fill all the details");
		return false;
	}
	else
	{
		return true;
	}
}