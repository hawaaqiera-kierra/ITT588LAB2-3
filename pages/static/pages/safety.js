// ===== Safety Check: Lab Work 3 =====

// ---------- Date and time handling ----------
document.body.appendChild(document.getElementById('resultModal'));
const now = new Date();
const hour = now.getHours();
// Ternary operator picks the greeting
const timeGreeting = hour < 12 ? 'Good morning' : hour < 18 ? 'Good afternoon' : 'Good evening';
document.getElementById('greeting').textContent =
  timeGreeting + '. It is ' + now.toLocaleDateString('en-MY', { weekday: 'long', day: 'numeric', month: 'long' }) + '.';

// ---------- Event loop demo (check the console order) ----------
console.log('1. Script started (synchronous)');
setTimeout(() => console.log('4. setTimeout callback (macrotask queue)'), 0);
Promise.resolve().then(() => console.log('3. Promise callback (microtask queue)'));
console.log('2. Script ended (synchronous)');

// ---------- Helpers ----------
function escapeHTML(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

let lastSummary = null;   // stores the latest result for the summary window

// ---------- Form handling ----------
const form = document.getElementById('safetyForm');

form.addEventListener('submit', function (event) {
  event.preventDefault();

  const name = document.getElementById('name').value.trim() || 'Friend';
  const safeChoice = form.querySelector('input[name="safe"]:checked');
  const errorBox = document.getElementById('formError');

  // Validation: control statement
  if (!safeChoice) {
    errorBox.textContent = 'Please tell us whether you are safe right now.';
    return;
  }
  errorBox.textContent = '';

  // Operators and loop: add up the ticked items
  let score = 0;
  let count = 0;
  const ticked = [];
  form.querySelectorAll('input[name="signs"]:checked').forEach(function (box) {
    score += Number(box.value);
    count++;
    ticked.push(box.nextElementSibling.textContent);
  });

  const inDanger = safeChoice.value === 'no';

  // if / else if / else: decide the level
  let level, colour, advice;
  if (inDanger || score >= 8) {
    level = 'High concern';  colour = 'danger';
    advice = 'Please contact help now. Call 999 if you are in immediate danger.';
  } else if (score >= 4) {
    level = 'Moderate concern'; colour = 'warning';
    advice = 'What you describe is serious. Talk to someone you trust and contact a hotline.';
  } else if (score > 0) {
    level = 'Some concern'; colour = 'info';
    advice = 'These are warning signs. Learn more and keep the hotline numbers close.';
  } else {
    level = 'No signs reported'; colour = 'success';
    advice = 'You did not report any signs. You can still read about GBV to support others.';
  }

  // switch: suggest a contact route
  const how = document.getElementById('how').value;
  let route;
  switch (how) {
    case 'call':     route = 'Call Talian Kasih 15999 or WAO 03-3000 8858.'; break;
    case 'whatsapp': route = 'WhatsApp Talian Kasih 019-261 5999 or WAO 018-988 8058.'; break;
    case 'report':   route = 'Lodge a report at any police station, or visit a hospital One Stop Crisis Centre.'; break;
    default:         route = 'See the Hotline page.';
  }

  const time = new Date().toLocaleTimeString('en-MY');
  lastSummary = { name, level, score, count, advice, route, ticked, time };

  // ---------- OUTPUT METHOD 1: innerHTML ----------
  document.getElementById('result').innerHTML =
    '<div class="soft-card border-' + colour + '" style="border-width:2px">' +
    '<h5>' + escapeHTML(name) + ', your result: <span class="text-' + colour + '">' + level + '</span></h5>' +
    '<p class="mb-2">' + advice + '</p>' +
    '<p class="mb-0"><strong>Suggested step:</strong> ' + route + '</p></div>';

  // ---------- OUTPUT METHOD 2: console ----------
  console.log('Result for', name, '->', level, '| score =', score);
  console.table(ticked.map(function (t, i) { return { no: i + 1, selected: t }; }));

  // ---------- OUTPUT METHOD 3: window.alert() ----------
  if (inDanger) {
    window.alert('If you are in immediate danger, call 999 now (112 from a mobile).');
  }

  // ---------- POPUP DIALOG: Bootstrap modal, shown after a short delay (event loop) ----------
  document.getElementById('modalBody').innerHTML =
    '<p><strong>' + level + '</strong> (score ' + score + ')</p><p>' + advice + '</p><p class="mb-0">' + route + '</p>';
  setTimeout(function () {
    bootstrap.Modal.getOrCreateInstance(document.getElementById('resultModal')).show();
  }, 600);
});

// ---------- OUTPUT METHOD 4: document.write() into a NEW window ----------
document.getElementById('summaryBtn').addEventListener('click', function () {
  if (!lastSummary) { return; }
  const s = lastSummary;
  const win = window.open('', '_blank', 'width=520,height=640');
  if (!win) { window.alert('Please allow pop-ups to open the summary.'); return; }
  win.document.write(
    '<html><head><title>Safety summary</title></head>' +
    '<body style="font-family:sans-serif;padding:24px">' +
    '<h2>Safety check summary</h2>' +
    '<p><strong>Name:</strong> ' + escapeHTML(s.name) + '</p>' +
    '<p><strong>Time:</strong> ' + s.time + '</p>' +
    '<p><strong>Level:</strong> ' + s.level + ' (score ' + s.score + ')</p>' +
    '<p>' + s.advice + '</p><p>' + s.route + '</p>' +
    '<p style="color:#666">Emergency: 999 | Talian Kasih: 15999</p>' +
    '</body></html>'
  );
  win.document.close();
});

// Clear button: reset the result area
document.getElementById('resetBtn').addEventListener('click', function () {
  document.getElementById('result').innerHTML = '';
  document.getElementById('formError').textContent = '';
  lastSummary = null;
  console.log('Form cleared');
});