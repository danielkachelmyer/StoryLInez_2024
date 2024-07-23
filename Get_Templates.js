const token = 'eyJraWQiOiIyMzY4ZjRhYi00N2ZiLTQwN2MtYjM5Ni00NzgxODcwMjZkN2UiLCJhbGciOiJSUzI1NiJ9.eyJqdGkiOiJhN2VvX3NGU1dZbzAtckQzdERKZWFBIiwiY2xpZW50X2lkIjoiT0MtQVpBVXhJWUlJTmtCIiwiYXVkIjoiaHR0cHM6Ly93d3cuY2FudmEuY29tIiwiaWF0IjoxNzIxNzA2OTIwLCJuYmYiOjE3MjE3MDY5MjAsImV4cCI6MTcyMTcyMTMyMCwiYnVuZGxlcyI6WyJDVDAyIl0sInRpZXIiOiJwYWlkIiwicm9sZXMiOiJJeV82ZFFjMy1mNUU0TnhnV1RnNk00RHUyd2I3OGJiTTREMDFKQ3lUaGRyY2JNVzJUUG1rUUZWdWZnQUxUVWJ0bmFVWnZfeldPbmJfRC1oZi1jSTNnN3h4Smo3dTFkQkNyZjdvUHREcmR0ZDNhZ3NHX0NYQ2NuRFpiVEo5OXVHU1VZUHpxdyIsImxvY2FsZSI6Im1sMVAzSnJPR3dDQTQzRTlCRm1ydWhRZ0g4cEpaTlBzS3c1UVRHZkpXTzlybW5VYkFkVFktVGprWjFTNHF4a05fQ1JxOFEiLCJzY29wZXMiOlsiYXNzZXQ6cmVhZCIsImFzc2V0OndyaXRlIiwiYnJhbmR0ZW1wbGF0ZTpjb250ZW50OnJlYWQiLCJicmFuZHRlbXBsYXRlOm1ldGE6cmVhZCIsImNvbW1lbnQ6cmVhZCIsImNvbW1lbnQ6d3JpdGUiLCJkZXNpZ246Y29udGVudDpyZWFkIiwiZGVzaWduOmNvbnRlbnQ6d3JpdGUiLCJkZXNpZ246bWV0YTpyZWFkIiwiZGVzaWduOnBlcm1pc3Npb246cmVhZCIsImRlc2lnbjpwZXJtaXNzaW9uOndyaXRlIiwiZm9sZGVyOnBlcm1pc3Npb246cmVhZCIsImZvbGRlcjpwZXJtaXNzaW9uOndyaXRlIiwiZm9sZGVyOnJlYWQiLCJmb2xkZXI6d3JpdGUiLCJwcm9maWxlOnJlYWQiXSwic3ViIjoib1VWT2pPNjd0VjMtVFdHeEw3cWNYUSIsImJyYW5kIjoib0JWT2otcXJxT3d3LS15cDdEVXF1ZyIsIm9yZ2FuaXphdGlvbiI6bnVsbCwiY29kZV9pZCI6ImkyRnZFSkdFNkRBYUVWRFVvanRCR1EifQ.dyItPOjwgqfe7ELTyqqie4oo0-lUfS_vhB0UOzTpYmsMFf5tPEch4Yv6q5sG21ffFzfA8bH_-ltaqNM6P7t3HCFfQB7aKKdrfJD5kcFC3wKzlTYKrvvlC_tee09Ibt2sFVQP0QuRzttbvecSyL9K65vRRr8Vcc4VHbLZd2zC4sJOjJneFFh3bR66rUzRlRFZLoKxEIPJSJ40s1MybTM1v7cHLvDBi2PhhKaP-gI0obkCsnEI_F4TK52jAWAH2W6AaUxie9a0VRxm-P8B86LN3f3JUN1w4jwdMyXIHPX4_pQAauwaDyXA1dclvEYH1zI9fblMjWChcKB4m_wHW-fnsg'

const Get_All_Templates=async()=>{
  try {
    const data=await fetch("https://api.canva.com/rest/v1/brand-templates", {method: "GET",headers: {  "Authorization": `Bearer ${token}`,}, })
    const response = await data.json()
    console.log(response);
  } catch (error) {
    console.log(error.message);
  }
}

//Get_All_Templates()

const Get_Template_ID=async(brandTemplateId)=>{
  try {
    const data=await fetch(`https://api.canva.com/rest/v1/brand-templates/${brandTemplateId}`, {  method: 'GET', headers: {   'Authorization': `Bearer ${token}`, }, })
    const res=await data.json();
    console.log(res);
  } catch (error) {
    console.log(error.message);
  }
}
Get_Template_ID("DAGLtZh_G3c")




//How to run the code: node Get_Templates.js
//uncomment the function call you want to see working
//Make sure to install node.js {Node.js is the standalone compiler for javascript without using broweser compiler}
