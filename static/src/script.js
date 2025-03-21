function colorCodeGroups() {
  console.log("script file found");
  let previousCode = "";
  let colorClass = "no-color-code";

  let manufacturerCodes = document.querySelectorAll(".manufacturer-code");

  for (const manufCode of manufacturerCodes) {
    const currentCode = manufCode.textContent;
    if (currentCode != previousCode) {
      if (colorClass == "no-color-code") {
        colorClass = "color-code";
      } else {
        colorClass = "no-color-code";
      }
    }
    manufCode.parentElement.classList.add(colorClass);
    previousCode = currentCode;
  }
}
colorCodeGroups();

document.querySelectorAll("input").forEach((input) => {
  input.addEventListener("keydown", function (event) {
    if (document.querySelector(".codeInFilter") && event.key === "Enter") {
      event.stopPropagation(); // Prevents the event from bubbling up to the div
    }
  });
});
