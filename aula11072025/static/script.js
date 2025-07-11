document.addEventListener('DOMContentLoaded', function() {

  document.body.className = "{{ tema }}";
  document.getElementById('tema').value = "{{ tema }}";
  
  document.getElementById('tema').addEventListener('change', function() {
      document.body.className = this.value;
      document.getElementById('tema').value = this.value;
  });

  document.getElementById('temaForm').addEventListener('submit', function(e) {
      
  });
});
