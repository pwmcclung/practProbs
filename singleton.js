class Singleton {
    constructor() {
        if (Singleton.instance) {
            return Singleton.instance;
        }

        this.data = {}; 
        Singleton.instance = this;
    }

    setData(key, value) {
        this.data[key] = value;
    }

    getData(key) {
        return this.data[key];
    }
}