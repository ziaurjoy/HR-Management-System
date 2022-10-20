
// DELETE FUNCTION SWEETALERT
console.log("I love Bangladesh")

function SweetDelete(e,href){
  e.preventDefault()
  var self = $(this)
  Swal.fire({
    title: 'Are you sure?',
    text: "You won't be able to revert this!",
    icon: 'question',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete it!'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Deleted!',
        'Your file has been deleted.',
        'success',
      )
      location.href = href
    }
  })
}