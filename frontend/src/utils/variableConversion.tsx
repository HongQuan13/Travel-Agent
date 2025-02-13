import _ from "lodash";

export const transformFrontendDataToBackend = (data: any): any => {
  if (_.isArray(data)) {
    return data.map((item) => transformFrontendDataToBackend(item));
  }

  if (_.isPlainObject(data)) {
    let transformedData = _.mapKeys(data, (_value, key) => _.snakeCase(key));

    transformedData = _.mapValues(transformedData, (value) => {
      if (_.isArray(value))
        return value.map((item) => transformFrontendDataToBackend(item));
      if (_.isPlainObject(value)) return transformFrontendDataToBackend(value);
      return value;
    });

    return transformedData;
  }

  return data;
};

export const transformBackendDataToFrontend = (data: any): any => {
  if (_.isArray(data)) {
    return data.map((item) => transformBackendDataToFrontend(item));
  }

  if (_.isPlainObject(data)) {
    let transformedData = _.mapKeys(data, (_value, key) => _.camelCase(key));

    transformedData = _.mapValues(transformedData, (value) => {
      if (_.isArray(value))
        return value.map((item) => transformBackendDataToFrontend(item));
      if (_.isPlainObject(value)) return transformBackendDataToFrontend(value);
      return value;
    });

    return transformedData;
  }

  return data;
};
