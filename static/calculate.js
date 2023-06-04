const inpAge = document.querySelector('#inputAge');
const inpRangeAge = document.querySelector('#rangeInputAge');
const inpPersent = document.querySelector('#inputPersent');
const inpRangePersent = document.querySelector('#rangeInputPersent');
const inpCredit = document.querySelector('#inputCredit');

const inputs = document.querySelectorAll('input');


const outputCredit = document.querySelector('#creditOut');
const outputPayment = document.querySelector('#paymentOut');


function calculate(){
	let total = (parseFloat(inpCredit.value) / (parseFloat(inpAge.value)*12.00)) + (parseFloat(inpCredit.value)*(parseFloat(inpPersent.value)*0.001));
	
	const formatter = new Intl.NumberFormat('ru', {maximumFractionDigits: 2});
	outputPayment.innerText = formatter.format(total);
	outputCredit.innerText = formatter.format(inpCredit.value);
}

calculate();

inpAge.addEventListener('input', function(){
	inpRangeAge.value = inpAge.value;
	calculate();
})

inpRangeAge.addEventListener('input', function(){
	inpAge.value = inpRangeAge.value;
	calculate();
})

inpPersent.addEventListener('input', function(){
	inpRangePersent.value = inpPersent.value;
	calculate();
})

inpRangePersent.addEventListener('input', function(){
	inpPersent.value = inpRangePersent.value;
	calculate();
})


for (const input of inputs){
	input.addEventListener('input', function(){
		calculate();
	})
}