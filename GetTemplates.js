
const token = 'asd';
const brandTemplateId = 'DEMzWSwy3BI';
fetch(`https://api.canva.com/rest/v1/brand-templates/${brandTemplateId}`, {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${token}`,
  },
})
.then(response => {
if (!response.ok) {
  throw new Error('Network response was not ok ' + response.statusText);
}
return response.json();
})
.then(data => {
console.log(data);
})
.catch(error => {
console.error('There was a problem with the fetch operation:', error);
});

//How to run: node filename.js
//Problem: Need token and brandTemplateId to get the templates 