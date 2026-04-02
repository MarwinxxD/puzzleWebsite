// Content for each hint - fill these in later
const hintContent = {
  1: "Content for Hint 1 coming soon.",
  2: "Content for Hint 2 coming soon.",
  3: "Content for Hint 3 coming soon.",
  4: "Content for Hint 4 coming soon.",
  5: "Content for Hint 5 coming soon.",
  6: "Content for Hint 6 coming soon.",
  7: "Content for Hint 7 coming soon.",
  8: "Content for Hint 8 coming soon.",
  9: "Content for Hint 9 coming soon.",
  10: "Content for Hint 10 coming soon.",
};

const modal = document.getElementById("modal");
const modalTitle = document.getElementById("modal-title");
const modalBody = document.getElementById("modal-body");
const modalClose = document.getElementById("modal-close");

let lastFocusedButton = null;

const focusableSelectors =
  'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';

function trapFocus(e) {
  const focusable = Array.from(modal.querySelectorAll(focusableSelectors));
  const first = focusable[0];
  const last = focusable[focusable.length - 1];

  if (e.shiftKey) {
    if (document.activeElement === first) {
      e.preventDefault();
      last.focus();
    }
  } else {
    if (document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }
}

function openModal(hintNumber, triggerButton) {
  lastFocusedButton = triggerButton;
  modalTitle.textContent = "Hint " + hintNumber;
  modalBody.textContent = hintContent[hintNumber] || "";
  modal.classList.add("open");
  modalClose.focus();
  modal.addEventListener("keydown", handleModalKeydown);
}

function closeModal() {
  modal.classList.remove("open");
  modal.removeEventListener("keydown", handleModalKeydown);
  if (lastFocusedButton) {
    lastFocusedButton.focus();
    lastFocusedButton = null;
  }
}

function handleModalKeydown(e) {
  if (e.key === "Escape") {
    closeModal();
  } else if (e.key === "Tab") {
    trapFocus(e);
  }
}

document.querySelectorAll(".hint-box").forEach(function (btn) {
  btn.addEventListener("click", function () {
    openModal(Number(btn.dataset.hint), btn);
  });
});

modalClose.addEventListener("click", closeModal);

modal.addEventListener("click", function (e) {
  if (e.target === modal) {
    closeModal();
  }
});
