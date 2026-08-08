import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Header Indicator
header_indicator = '''
        <div class="flex items-center gap-4">
            <div class="hidden md:flex items-center gap-2 bg-[#dcfce7] text-[#166534] px-3 py-1.5 rounded-full text-sm font-bold shadow-sm">
                <span class="material-symbols-outlined text-[18px]">hub</span>
                Active Hub: Kankavli (Pincode: 416602)
            </div>
'''
content = re.sub(r'(<div class="flex items-center gap-4">)', header_indicator, content, count=1)

# 2. Add Pincode Field to Add Product Form
add_pincode_field = '''
            <div>
                <label class="form-label">Target Pincode / Service Area</label>
                <input type="text" id="p_pincode" class="form-input" value="416602" readonly>
            </div>
'''
content = re.sub(r'(<form id="addProductForm" class="flex flex-col gap-4">)', r'\1' + add_pincode_field, content)

# 3. Add Pincode Field to Edit Product Form
edit_pincode_field = '''
            <div>
                <label class="form-label">Target Pincode / Service Area</label>
                <input type="text" id="e_pincode" class="form-input" value="416602" readonly>
            </div>
'''
content = re.sub(r'(<form id="editProductForm" class="flex flex-col gap-4">)', r'\1' + edit_pincode_field, content)

# 4. Add Service Area badge to Product Cards
service_area_badge = '''<div class="mt-2 text-xs font-bold bg-[#E8F5E9] text-[#10B981] inline-flex items-center gap-1 px-2 py-1 rounded w-fit"><span class="material-symbols-outlined text-[14px]">my_location</span>Service Area: 416602 (Kankavli)</div>'''

# Inject right after the product name `displayName` or description in `card.innerHTML`
content = re.sub(r'(<div class="text-sm font-semibold text-\[\#1a1a2e\] truncate">\$\{product\.name_en \|\| product\.name\}</div>)', r'\1\n                                ' + service_area_badge, content)
# Wait, let me check the exact string for product name in admin.html first... 
# Actually, the string for product name in admin.html is likely `<div class="text-sm font-semibold text-[#1a1a2e] truncate">${product.name_en || product.name || 'Unnamed'}</div>`
