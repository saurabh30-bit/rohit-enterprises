import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Navigation Pill to top nav
pill_html = '''
    <div id="nav-location-pill" class="hidden sm:flex items-center gap-2 text-sm font-label-md text-on-surface hover:text-primary transition-colors bg-surface-container-low px-3 py-1.5 rounded-full border border-outline-variant cursor-pointer">
        <span class="material-symbols-outlined text-[16px] text-primary">location_on</span>
        <span>Delivering to: <span id="nav-pincode">416602</span> (Kankavli)</span>
    </div>
'''

content = re.sub(r'(<div class="flex items-center space-x-4">)', r'\1\n' + pill_html, content)

# 2. Add Location Modal to body
modal_html = '''
<!-- Location Modal -->
<div id="locationModal" class="fixed inset-0 bg-black/60 hidden flex items-center justify-center z-[200] p-4 transition-opacity duration-300 opacity-0">
    <div class="bg-surface rounded-2xl shadow-2xl max-w-md w-full p-8 relative transform scale-95 transition-transform duration-300">
        <div class="text-center mb-6">
            <div class="w-16 h-16 bg-primary/10 text-primary rounded-full flex items-center justify-center mx-auto mb-4">
                <span class="material-symbols-outlined text-4xl">location_on</span>
            </div>
            <h2 class="font-headline-md text-2xl text-on-background font-bold mb-2">Enter your Pincode to view available local inventory</h2>
            <p class="font-body-md text-on-surface-variant">Currently serving Kankavli & surrounding regional hubs in Sindhudurg</p>
        </div>
        <div class="flex flex-col gap-4">
            <input type="text" id="pincodeInput" value="416602" placeholder="Enter Pincode" class="w-full p-4 border-2 border-outline-variant rounded-xl bg-surface focus:border-primary focus:outline-none text-center text-xl font-bold tracking-widest text-on-surface transition-colors">
            <button id="confirmLocationBtn" class="w-full bg-primary text-on-primary py-4 rounded-xl font-bold hover:opacity-90 transition-opacity text-lg shadow-lg flex items-center justify-center gap-2">
                Confirm Location
                <span class="material-symbols-outlined">arrow_forward</span>
            </button>
        </div>
    </div>
</div>
'''

content = re.sub(r'(<div id="cart-backdrop")', modal_html + r'\n\1', content)

# 3. Add location logic to JS
js_logic = '''
        // --- LOCATION LOGIC ---
        const locationModal = document.getElementById('locationModal');
        const confirmLocationBtn = document.getElementById('confirmLocationBtn');
        const pincodeInput = document.getElementById('pincodeInput');
        const navLocationPill = document.getElementById('nav-location-pill');
        const navPincode = document.getElementById('nav-pincode');
        
        function openLocationModal() {
            locationModal.classList.remove('hidden');
            setTimeout(() => {
                locationModal.classList.remove('opacity-0');
                locationModal.querySelector('div').classList.remove('scale-95');
            }, 10);
        }
        
        function closeLocationModal() {
            locationModal.classList.add('opacity-0');
            locationModal.querySelector('div').classList.add('scale-95');
            setTimeout(() => locationModal.classList.add('hidden'), 300);
        }
        
        const savedPincode = localStorage.getItem('userPincode');
        if (!savedPincode) {
            openLocationModal();
        } else {
            if(navPincode) navPincode.textContent = savedPincode;
            if(pincodeInput) pincodeInput.value = savedPincode;
        }
        
        if (confirmLocationBtn) {
            confirmLocationBtn.addEventListener('click', () => {
                const code = pincodeInput.value.trim() || '416602';
                localStorage.setItem('userPincode', code);
                if(navPincode) navPincode.textContent = code;
                closeLocationModal();
            });
        }
        
        if (navLocationPill) {
            navLocationPill.addEventListener('click', openLocationModal);
        }
'''

content = re.sub(r'(// --- CART LOGIC ---)', js_logic + r'\n\n        \1', content)

# 4. Inject delivery badges on product cards
badge_html = '''<div class="mt-2 mb-3 bg-[#E8F5E9] text-[#10B981] text-xs font-bold px-2 py-1 rounded inline-flex items-center gap-1 w-fit"><span class="material-symbols-outlined text-[14px]">bolt</span>Express 2-Hour Delivery in 416602</div>'''

# Need to inject after the h3 or before the price. Let's put it after the h3.
content = re.sub(r'(<h3 class="font-headline-sm text-headline-sm text-on-background mb-1 md:mb-[^"]*text-sm md:text-xl truncate">\${display[^}]+}</h3>)', r'\1\n                    ' + badge_html, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated index.html location features.')
