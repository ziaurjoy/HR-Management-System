

$(document).ready(function() {
  $("#id_user").select2({
  });
});


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


$("#id_branch").change(function () {
  var branchId = $(this).val();  
  $.ajax({                       
    url: ajax_load_branch_users_url,
    
    data: {
      'branchId': branchId   
    },
    success: function (data) { 
      $("#id_user").html(data);  
      }
  }); 
});


$("#id_user").change(function () {
  var userId = $(this).val();  
  $.ajax({                       
    url: ajax_load_user_wise_permission_url,
    
    data: {
      'userId': userId 
    },
    success: function (data) { 
      $("#id_permission").html(data);  
      console.log('Clicked');
      }
  }); 
});

