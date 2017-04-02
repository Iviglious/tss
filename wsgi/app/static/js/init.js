// This is the init.js

$('.datepicker').pickadate({
    format: 'yyyy-mm-dd',
    formatLabel: 'yyyy-mm-dd',
    formatSubmit: 'yyyy-mm-dd',
    hiddenPrefix: 'prefix__',
    hiddenSuffix: '__suffix',
    closeOnSelect: true,
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15 // Creates a dropdown of 15 years to control year
  });