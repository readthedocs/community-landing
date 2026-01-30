// Trigger the Read the Docs search addon from the landing page search input.
(function () {
  const selector = "#rtd-search-input";

  function triggerSearchAddon() {
    let event;
    if (typeof CustomEvent === "function") {
      event = new CustomEvent("readthedocs-search-show");
    } else {
      event = document.createEvent("CustomEvent");
      event.initCustomEvent("readthedocs-search-show", true, true, {});
    }
    document.dispatchEvent(event);
  }

  document.addEventListener("DOMContentLoaded", function () {
    const input = document.querySelector(selector);
    if (!input) {
      return;
    }

    input.addEventListener("click", triggerSearchAddon);
    input.addEventListener("focus", triggerSearchAddon);
  });
})();
