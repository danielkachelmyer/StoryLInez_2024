const token = 'eyJraWQiOiIyMzY4ZjRhYi00N2ZiLTQwN2MtYjM5Ni00NzgxODcwMjZkN2UiLCJhbGciOiJSUzI1NiJ9.eyJqdGkiOiJzWmthb3ZBZl9RYkJZT3VPaTVlMnlRIiwiY2xpZW50X2lkIjoiT0MtQVpBVXhJWUlJTmtCIiwiYXVkIjoiaHR0cHM6Ly93d3cuY2FudmEuY29tIiwiaWF0IjoxNzIxNjg1NDc2LCJuYmYiOjE3MjE2ODU0NzYsImV4cCI6MTcyMTY5OTg3NiwiYnVuZGxlcyI6WyJQUk9TIl0sInRpZXIiOiJwYWlkIiwicm9sZXMiOiJtOEhuR3FheUlKeWlMYTVxMjF0dG9RcmNiY180SEpMQjB1eFRtNHNSSEx2SG5zLVlmM213dEpSMFJ6eVRXYjQyWHdDLVNlSURNdUt4eER5Mkk4Y2xoSnV0Q2VGeHZQZ2xjaTY5QnJleDNLNzZnQlpCWUFiZHBOZVFncWZpMDVJN0pXanA2SlNUZWxzYl9pLUdTYkE4WjU0UU93OCIsImxvY2FsZSI6Ims5Y0NqanNNeGViUHo4ZUlZZlozTVZRY3hKOVdMWHBIbTNMQ3pHRXc5bXNkc2hHSkhRT1BhSHZDN2R1aTdnTEdlSGJMOUEiLCJzY29wZXMiOlsiYXNzZXQ6cmVhZCIsImFzc2V0OndyaXRlIiwiYnJhbmR0ZW1wbGF0ZTpjb250ZW50OnJlYWQiLCJicmFuZHRlbXBsYXRlOm1ldGE6cmVhZCIsImNvbW1lbnQ6cmVhZCIsImNvbW1lbnQ6d3JpdGUiLCJkZXNpZ246Y29udGVudDpyZWFkIiwiZGVzaWduOmNvbnRlbnQ6d3JpdGUiLCJkZXNpZ246bWV0YTpyZWFkIiwiZGVzaWduOnBlcm1pc3Npb246cmVhZCIsImRlc2lnbjpwZXJtaXNzaW9uOndyaXRlIiwiZm9sZGVyOnBlcm1pc3Npb246cmVhZCIsImZvbGRlcjpwZXJtaXNzaW9uOndyaXRlIiwiZm9sZGVyOnJlYWQiLCJmb2xkZXI6d3JpdGUiLCJwcm9maWxlOnJlYWQiXSwic3ViIjoib1VWT2pPNjd0VjMtVFdHeEw3cWNYUSIsImJyYW5kIjoib0JWT2otcXJxT3d3LS15cDdEVXF1ZyIsIm9yZ2FuaXphdGlvbiI6bnVsbCwiY29kZV9pZCI6IloxeWJ3cGVUcmVOYXVwZTZYaFUyeHcifQ.Yr-LLPNCEHnbkMbxCLoMLANcyfiXHvFCoP3L9y9Sum6Jc6CU5FAbu4ekpO34w-gckkBMo6MtsPEybvKiEs9CdlhfgCWVTFLsCYeCwYNKAWG7pkuI7kx-pUc5eWy8J-o2_JEzyz-DrYWknMf94FyG0j3ahELX_GuBv1cDudRmv-8Jk45claBzFsMKAzvzVPDRwfFvcPbMNmrazRXB4JNHOgWrRVrxI8JUmZNfL_8asOt_PUaFzJVZdzIwdXFWODWDSuyMyxcqYzdxd8LK_RZWHLpxPwl-vdQbq4G4uyu_Ai7SLPeYp6Ry_xiDZ3VNcEA22smOQGpAtZLZ4f99m5fKeA';

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

const Get_Template_ID=async(ID)=>{
  try {
    const brandTemplateId="DAGLtZh_G3c"
    const data=await fetch(`https://api.canva.com/rest/v1/brand-templates/${brandTemplateId}`, {  method: 'GET', headers: {   'Authorization': `Bearer ${token}`, }, })
    const res=await data.json();
    console.log(res);
  } catch (error) {
    console.log(error.message);
  }
}
//Get_Template_ID()




//How to run the code: node Get_Templates.js
//uncomment the function call you want to see working
//Make sure to install node.js {Node.js is the standalone compiler for javascript without using broweser compiler}