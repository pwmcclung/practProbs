function uniteUnique(...arr) {
    let listed = [...arr].flat();
   return [...new Set(listed)]
  }