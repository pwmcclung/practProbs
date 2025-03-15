class UriBuilder {
    constructor(uri) {
      this.uri = uri;
      this.params = {};
  
      const [baseUrl, queryString] = uri.split('?');
      this.baseUrl = baseUrl;
  
      if (queryString) {
        queryString.split('&').forEach(param => {
          const [key, value] = param.split('=');
          this.params[key] = value;
        });
      }
    }
  
    build() {
      const paramsArray = [];
      for (const key in this.params) {
        if (this.params.hasOwnProperty(key)) {
            if (Array.isArray(this.params[key])) {
                this.params[key].forEach(value => {
                    paramsArray.push(`${encodeURIComponent(key)}=${encodeURIComponent(value)}`);
                });
            } else {
                paramsArray.push(`${encodeURIComponent(key)}=${encodeURIComponent(this.params[key])}`);
            }
        }
      }
  
      if (paramsArray.length > 0) {
        return `${this.baseUrl}?${paramsArray.join('&')}`;
      } else {
        return this.baseUrl;
      }
    }
  }