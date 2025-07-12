// DOM Ready
document.addEventListener('DOMContentLoaded', function() {
    initMobileMenu();
    initAuthForms();
    initItemInteractions();
    initSwapLogic();
});

// Mobile Menu Toggle
function initMobileMenu() {
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }
}

// Auth Forms Placeholder (Define if needed)
function initAuthForms() {
    // Add form toggle/login/register logic if applicable
}

// Item Interactions (Favorite, View Details)
function initItemInteractions() {
    document.querySelectorAll('.item-favorite').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            this.classList.toggle('active');
            const itemId = this.dataset.itemId;
            console.log(`Toggled favorite for item ${itemId}`);
            // TODO: AJAX call to update favorite status
        });
    });
}

// Swap Logic
function initSwapLogic() {
    // Swap proposal buttons
    document.querySelectorAll('.btn-propose-swap').forEach(btn => {
        btn.addEventListener('click', function() {
            const itemId = this.dataset.itemId;
            openSwapModal(itemId);
        });
    });
    
    // Swap confirmation
    const swapConfirm = document.getElementById('confirm-swap');
    if (swapConfirm) {
        swapConfirm.addEventListener('click', function() {
            const swapData = {
                offeredItem: document.getElementById('swap-offered-item').value,
                requestedItem: document.getElementById('swap-requested-item').value,
                message: document.getElementById('swap-message').value
            };
            console.log('Swap proposed:', swapData);
            // TODO: AJAX call to submit swap
        });
    }
}

function openSwapModal(itemId) {
    console.log(`Opening swap modal for item ${itemId}`);
    // TODO: Show modal with form to select an item to offer in exchange
}
