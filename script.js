document.getElementById('ckdForm').addEventListener('submit', function(e) {
  e.preventDefault();

  // Get input values
  const age = parseFloat(document.getElementById('age').value);
  const bp = parseFloat(document.getElementById('bp').value);
  const al = parseFloat(document.getElementById('al').value);
  const su = parseFloat(document.getElementById('su').value);
  const hemo = parseFloat(document.getElementById('hemo').value);

  // Simple rule-based check (for demo only)
  let risk = 0;
  if(bp > 140) risk++;
  if(al > 3.5) risk++;
  if(su > 140) risk++;
  if(hemo < 10) risk++;

  let result = '';
  if(risk >= 2) {
    result = "<span style='color: red;'>High risk of CKD. Please consult a doctor.</span>";
  } else {
    result = "<span style='color: green;'>Low risk of CKD.</span>";
  }

  document.getElementById('result').innerHTML = result;
});
