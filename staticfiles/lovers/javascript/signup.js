/*Username length check*/

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#username').onkeyup=() =>{
        const username=document.querySelector('#username').value;
        if (username.length<4 && username.length!==0) {
            document.querySelector('#lengthcheck').innerHTML= ('name too short');
        }
        else{
            document.querySelector('#lengthcheck').innerHTML= ('baaaaaaaad');
        }


    }
  
})