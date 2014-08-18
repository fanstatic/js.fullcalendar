/*
 * File Name : fullcalendar_fr.js
 *
 */
// fullcalendar french translations
var localOptions={
  buttonText:{
    today:"Aujourd'hui",
    month:"Mois",
    day:"Jour",
    week:"Semaine"
  },
  monthNames: ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"],
  monthNamesShort:["Jan","Fev","Mar","Avr","Mai","Juin","Juil","Aoû","Sept","Oct","Nov","Déc"],
  dayNames:["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"],
  dayNamesShort:["Di","Lu","Ma","Me","Je","Ve","Sa"],
  firstDay:1,
  titleFormat: {
      month: 'MMMM yyyy',
      week: "dd. MMMM yyyy {'&#8212;' dd. MMMM yyyy}",
      day: 'dddd, d. MMMM yyyy'
  },
  columnFormat: {
      month: 'ddd',
      week: 'ddd dd.MM.',
      day: ''
  },
  timeFormat: { // for event elements
      '': 'HH:mm',
      agenda: 'HH:mm{ - HH:mm}'
  },
  allDayText: 'Sur la journée',
  axisFormat: 'HH:mm'
};
