

$("#id_mother_organization").change(function () { 
  var mother_organizationId = $(this).val();  
  $.ajax({                       
  url: ajax_load_sister_organization_url,
  data: {
    'mother_organization_id': mother_organizationId   
  },
  success: function (data) { 
    $("#id_sister_organization").html(data);  
    }
  });
});



$("#id_sister_organization").change(function () {
  var sister_organizationId = $(this).val();  
  $.ajax({                       
    url: ajax_load_branch_url,
    data: {
    'sister_organization_id': sister_organizationId   
    },
    success: function (data) { 
    $("#id_branch").html(data);  
    }
  }); 
});
