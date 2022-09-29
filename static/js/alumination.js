AOS.init();

var element = document.getElementsByClassName("chartcircles")[0];
var chartsShowed = false;
function circleprogress(i, progressi)
{
	var ctx = document.getElementsByClassName('progress')[i].getContext("2d");
var al = 0;
var start = 4.72;
var cw = ctx.canvas.width;
var ch = ctx.canvas.height; 
var diff;
function progressSim(){;
	diff = ((al/ 100) * Math.PI*2*10).toFixed(2);
	ctx.clearRect(0, 0, cw, ch);
	ctx.lineWidth = 10;
	ctx.fillStyle = '#c5c7c7';
	ctx.strokeStyle = "#f2c351";
	ctx.font = "30px Roboto"
	ctx.textAlign = 'center';
	ctx.fillText(al+'%', cw*.5, ch*.5, cw);
	ctx.beginPath();
	ctx.arc(cw*0.5, ch*0.5, 130, start, (diff/10)+start, false);
	ctx.stroke();
	if(al >= progressi){
		clearTimeout(sim);
	    // Add scripting here that will run when progress completes
	}
	al++;
}
var sim = setInterval(progressSim, 25);
}
// var progress = [71, 89, 81, 62];
// for(var i=0; i<4; i++)
// circleprogress(i, progress[i]);





function isOnScreen(element)
{
	const rect = element.getBoundingClientRect();

	return (
        (rect.top >= 0 &&
        rect.left >= 0) ||
        (rect.bottom <= (window.innerHeight) &&
         rect.right <= (window.innerWidth))

    );
}

function displayChart(element, chartsShowed1)
{
	if(!chartsShowed1 && isOnScreen(element))
	{
	var progress = [71, 89, 81, 62];
	for(var i=0; i<3; i++) 
	{
		circleprogress(i, progress[i]);
	}
	chartsShowed = true;
	}
	// console.log("isOnScreen(element)");
}


document.addEventListener("scroll", () => {
	displayChart(element, chartsShowed);
});



// $('window').scroll(function(){
//   \
// })



























const docStyle = document.documentElement.style;
const aElem = document.querySelector('a');
const boundingClientRect = aElem.getBoundingClientRect();

aElem.onmousemove = function (e) {

  const x = e.clientX - boundingClientRect.left;
  const y = e.clientY - boundingClientRect.top;

  const xc = boundingClientRect.width / 2;
  const yc = boundingClientRect.height / 2;

  const dx = x - xc;
  const dy = y - yc;

  docStyle.setProperty('--rx', `${dy / -1 + 10}deg`);
  docStyle.setProperty('--ry', `${dx / 10 - 10}deg`);

};

aElem.onmouseleave = function (e) {

  docStyle.setProperty('--ty', '0');
  docStyle.setProperty('--rx', '0');
  docStyle.setProperty('--ry', '0');

};

aElem.onmousedown = function (e) {

  docStyle.setProperty('--tz', '-25px');

};

document.body.onmouseup = function (e) {

  docStyle.setProperty('--tz', '-12px');

};