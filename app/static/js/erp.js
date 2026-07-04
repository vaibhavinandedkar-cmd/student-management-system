document.addEventListener('DOMContentLoaded', function () {
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.querySelector('.sidebar');

    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', function () {
            sidebar.classList.toggle('collapsed');
        });
    }

    // Quick Add Student modal handlers
    const quickSave = document.getElementById('quickStudentSave');
    const quickForm = document.getElementById('quickStudentForm');
    const quickError = document.getElementById('quickStudentError');

    function showToast(message, variant = 'success') {
        const container = document.querySelector('.toast-container');
        if (!container) return;
        const toastEl = document.createElement('div');
        toastEl.className = `toast align-items-center text-bg-${variant} show`; 
        toastEl.setAttribute('role','alert');
        toastEl.innerHTML = `<div class="d-flex"><div class="toast-body">${message}</div><button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button></div>`;
        container.appendChild(toastEl);
        setTimeout(() => {
            try { toastEl.remove(); } catch(e){}
        }, 5000);
    }

    async function submitQuickStudent() {
        if (!quickForm) return;
        quickError.style.display = 'none';
        const formData = new FormData(quickForm);
        const payload = {};
        formData.forEach((v,k) => payload[k] = v);

        try {
            const res = await fetch('/api/v1/students/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            if (!res.ok) {
                quickError.textContent = (data.errors && JSON.stringify(data.errors)) || data.message || 'Failed to create student';
                quickError.style.display = 'block';
                return;
            }

            // Success
            const modalEl = document.getElementById('quickStudentModal');
            const bsModal = bootstrap.Modal.getInstance(modalEl);
            if (bsModal) bsModal.hide();
            quickForm.reset();
            showToast('Student created successfully.', 'success');
            // Optionally refresh page or update counter
            const studentsCounter = document.querySelector('h2.mb-0');
            if (studentsCounter) {
                const n = parseInt(studentsCounter.textContent || '0', 10) || 0;
                studentsCounter.textContent = n + 1;
            }
        } catch (err) {
            quickError.textContent = err.message || 'Network error';
            quickError.style.display = 'block';
        }
    }

    if (quickSave) {
        quickSave.addEventListener('click', submitQuickStudent);
    }
});
