import _ from "lodash";

export const transformFrontendDataToBackend = (data: any): any => {
  let transformedData;

  if (Array.isArray(data)) {
    transformedData = data.map((item) => transformFrontendDataToBackend(item));
  }

  if (_.isObject(data)) {
    transformedData = _.mapKeys(data, (_value, key) => _.snakeCase(key));
    transformedData = _.mapValues(transformedData, (value) => {
      if (_.isArray(value) || _.isObject(value))
        return transformFrontendDataToBackend(value);
      return value;
    });
  }

  return transformedData;
};

export const transformBackendDataToFrontend = (data: any): any => {
  let transformedData;

  if (_.isArray(data)) {
    return data.map((item) => transformBackendDataToFrontend(item));
  }

  if (_.isObject(data)) {
    transformedData = _.mapKeys(data, (_value, key) => _.camelCase(key));
    transformedData = _.mapValues(transformedData, (value) => {
      if (_.isArray(value) || _.isObject(value))
        return transformBackendDataToFrontend(value);
      return value;
    });
  }

  return transformedData;
};
