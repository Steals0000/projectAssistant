const inp = document.querySelector('#square-input');
console.log(inp);
const inpR = document.querySelector('#square-range');
console.log(inpR);
const outputPrice = document.querySelector('#total-price');
console.log(outputPrice);


function calculate(){
	let totalPrice =  0.3 * parseFloat(inp.value);
	console.log(totalPrice);
	
	const formatter = new Intl.NumberFormat('ru', {maximumFractionDigits: 2});
	outputPrice.innerText = formatter.format(totalPrice);
}

calculate();

inpR.addEventListener('input', function(){
	inp.value = inpR.value;
	calculate();
})

inp.addEventListener('input', function(){
	inpR.value = inp.value;
	calculate();
})