let url="http://api.weatherapi.com/v1/current.json?key=addfe7cd16e945ac88a103517230809=kochi"

fetch(url).then((res)=>res.json()).then(data=>console.log(data));
const cloudOutput=document.querySelector(".cloud")
const humidityOutput=document.querySelector(".humidity")
const windOutput=document.querySelector(".wind")
const app=document.querySelector(".weatherapp")
const temp=document.querySelector(".temp")

function fetchweather(){
  const form = document.getElementById('locationInput');
const cityInput = document.getElementById('id_city');

form.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent form submission

  var cityName = cityInput.value;
  console.log(cityName);
  // Perform further operations with the cityName value
  
  // Clear the input field after retrieving the value
  cityInput.value = '';

  fetch(`http://api.weatherapi.com/v1/current.json?key=addfe7cd16e945ac88a103517230809&q=${cityName}`).then(res=>res.json()).then(data=>displayweather(data))
});

 
}
function displayweather(data){

  let name=data.location.name
  let icon=data.current.condition.icon
  let desc=data.current.condition.text
  let temp=data.current.temp_c
  let humidity=data.current.humidity
  let tim=data.current.last_updated
  
  console.log(name,icon,temp,desc,humidity);

  htmlData=`
  
  
  <h3 class="brand">the Weather</h3>
  <div>
      <h1 class="temp">${temp}° </h1>
      <div class="city-time">
          <h1 class="name">${name}</h1>
          <small>
              
              <span class="date">${tim}</span>
          </small>
      </div>
      <div class="weather">
          <img src="${icon}" alt="" width="50" height="50">
          <span class="condition">${desc}</span>
      </div>
  </div>


  `
 

  
  document.querySelector("#id_result").innerHTML=htmlData
  cloudOutput.innerHTML=data.current.cloud + "%"
  humidityOutput.innerHTML=data.current.humidity + "%"
  windOutput.innerHTML=data.current.wind_kph + "km/h"

 
  
}








