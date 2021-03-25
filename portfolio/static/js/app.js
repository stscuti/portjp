const texto = document.getElementById('logo');
const objetivo = document.getElementById('logotipo');
const letras = texto.innerText.split("");

texto.innerText = '';

letras.forEach((letra) =>{
	let caracter = letra === ' ' ? '&nbsp;' : letra;

    texto.innerHTML = texto.innerHTML + `
        <div>
            <span>${caracter}</span>
            <span class="segunda-linea">${caracter}</span>
        </div>
    `;

} );

objetivo.addEventListener('mouseenter', () => {
	let cuenta = 0;

	const intervalo = setInterval(() =>{
        if(cuenta < texto.children.length){
        	texto.children[cuenta].classList.add('animacion');
        	cuenta +=1;
        } else{
        	clearInterval(intervalo);
        }
        
	}, 5);
});

objetivo.addEventListener('mouseleave', () => {
	let cuenta = 0;

	const intervalo = setInterval(() =>{
        if(cuenta < texto.children.length){
        	texto.children[cuenta].classList.remove('animacion');
        	cuenta +=1;
        } else{
        	clearInterval(intervalo);
        }
        
	}, 5);
});