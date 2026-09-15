document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('random-place-card');
    const triggerBtn = document.getElementById('random-place-btn');
    if (!container || !triggerBtn) return;

    function escapeHtml(value) {
        return String(value ?? '').replace(/[&<>"']/g, (c) => ({
            '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
        }[c]));
    }

    function formatCreatedAt(isoString) {
        const date = new Date(isoString);
        if (Number.isNaN(date.getTime())) return '';
        const datePart = date.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' });
        const timePart = date.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit', hour12: false });
        return `${datePart}, ${timePart}`;
    }

    function renderCard(place) {
        if (!place) {
            container.innerHTML = '<p class="places-empty-inline">No places yet — add one!</p>';
            return;
        }
        const stars = '★'.repeat(place.rating) + '☆'.repeat(5 - place.rating);
        const detailUrl = `/places/${encodeURIComponent(place.id)}/`;
        container.innerHTML = `
            <a class="place-card" href="${escapeHtml(detailUrl)}">
                <img class="place-card-photo" src="/static/${escapeHtml(place.photo || 'gopher-train.png')}" alt="${escapeHtml(place.name)}">
                <div class="place-card-body">
                    <div class="place-card-top">
                        <h2 class="place-card-name">${escapeHtml(place.name)}</h2>
                        <span class="place-card-rating" title="${place.rating} out of 5">${stars}</span>
                    </div>
                    <div class="place-card-meta">
                        ${place.place_type ? `<span class="place-card-type">${escapeHtml(place.place_type)}</span>` : ''}
                        ${place.location ? `<span class="place-card-location">${escapeHtml(place.location)}</span>` : ''}
                    </div>
                    ${place.description ? `<p class="place-card-description">${escapeHtml(place.description)}</p>` : ''}
                    ${place.created_at ? `<p class="place-card-created-at">Added ${escapeHtml(formatCreatedAt(place.created_at))}</p>` : ''}
                </div>
            </a>
        `;
    }

    async function loadRandomPlace() {
        triggerBtn.disabled = true;
        try {
            const res = await fetch('/places/random/');
            const data = await res.json();
            renderCard(data.place);
        } finally {
            triggerBtn.disabled = false;
        }
    }

    triggerBtn.addEventListener('click', loadRandomPlace);
});
