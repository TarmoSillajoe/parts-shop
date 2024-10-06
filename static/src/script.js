let previousCode = "";
let colorClass = "no-color";

let manufacturerCodes = document.querySelectorAll(".manufacturer-code");

for (const manufCode of manufacturerCodes) {
  const currentCode = manufCode.textContent;
  if (currentCode != previousCode) {
    if (colorClass == "no-color") {
      colorClass = "bg-indigo-500";
    } else {
      colorClass = "no-color";
    }
  }
  manufCode.parentElement.classList.add(colorClass);
  previousCode = currentCode;
}
