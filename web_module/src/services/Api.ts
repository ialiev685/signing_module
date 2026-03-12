/* eslint-disable */
/* tslint:disable */
// @ts-nocheck
/*
 * ---------------------------------------------------------------
 * ## THIS FILE WAS GENERATED VIA SWAGGER-TYPESCRIPT-API        ##
 * ##                                                           ##
 * ## AUTHOR: acacode                                           ##
 * ## SOURCE: https://github.com/acacode/swagger-typescript-api ##
 * ---------------------------------------------------------------
 */

/** StoreNamePathModel */
export enum StoreNamePathModel {
  MRoot = "mRoot",
  MCA = "mCA",
}

/** Body_create_hash_api_v1_create_hash_post */
export interface BodyCreateHashApiV1CreateHashPost {
  /**
   * File
   * @format binary
   */
  file: File;
}

/** Body_set_personal_certificates_api_v1_set_certificate__store_name__post */
export interface BodySetPersonalCertificatesApiV1SetCertificateStoreNamePost {
  /**
   * Certificate
   * Загрузите файл
   * @format binary
   */
  certificate: File;
}

/** Body_verify_signature_api_v1_verify_signature_post */
export interface BodyVerifySignatureApiV1VerifySignaturePost {
  /**
   * Document
   * Загрузите подписанный документ
   * @format binary
   */
  document: File;
  /**
   * Detached Signature
   * Загрузите открепленную подпись
   * @format binary
   */
  detached_signature: File;
}

/** CertificateInfoModel */
export interface CertificateInfoModel {
  /** Subject Name */
  subject_name?: string | null;
  /** Issuer Name */
  issuer_name: string;
  /** Thumbprint */
  thumbprint?: string | null;
  /** Valid From Date */
  valid_from_date?: string | null;
  /** Valid To Date */
  valid_to_date?: string | null;
  /** Serial Number */
  serial_number?: string | null;
  /** Oids */
  oids?: string[] | null;
}

/** HTTPValidationError */
export interface HTTPValidationError {
  /** Detail */
  detail?: ValidationError[];
}

/** RemoveCertificateBodyModel */
export interface RemoveCertificateBodyModel {
  /** Thumbprint */
  thumbprint: string;
  store_name: StoreNamePathModel;
}

/** ResponseDataModel */
export interface ResponseDataModel {
  /**
   * Has Error
   * @default false
   */
  has_error?: boolean | null;
  /** Error */
  error?: null;
  /** Data */
  data?: null;
}

/** ResponseDataModel[CertificateInfoModel] */
export interface ResponseDataModelCertificateInfoModel {
  /**
   * Has Error
   * @default false
   */
  has_error?: boolean | null;
  /** Error */
  error?: null;
  data?: CertificateInfoModel | null;
}

/** ResponseDataModel[NoneType] */
export interface ResponseDataModelNoneType {
  /**
   * Has Error
   * @default false
   */
  has_error?: boolean | null;
  /** Error */
  error?: null;
  /** Data */
  data?: null;
}

/** ResponseDataModel[VerificationModel] */
export interface ResponseDataModelVerificationModel {
  /**
   * Has Error
   * @default false
   */
  has_error?: boolean | null;
  /** Error */
  error?: null;
  data?: VerificationModel | null;
}

/** ResponseDataModel[list[CertificateInfoModel]] */
export interface ResponseDataModelListCertificateInfoModel {
  /**
   * Has Error
   * @default false
   */
  has_error?: boolean | null;
  /** Error */
  error?: null;
  /** Data */
  data?: CertificateInfoModel[] | null;
}

/** SignersModel */
export interface SignersModel {
  /** Subject Name */
  subject_name?: string | null;
  /** Issuer Name */
  issuer_name: string;
  /** Thumbprint */
  thumbprint?: string | null;
  /** Valid From Date */
  valid_from_date?: string | null;
  /** Valid To Date */
  valid_to_date?: string | null;
  /** Serial Number */
  serial_number?: string | null;
  /** Oids */
  oids?: string[] | null;
  /** Signature Timestamp Time */
  signature_timestamp_time?: string | null;
  /** Signing Time */
  signing_time?: string | null;
}

/** SigningStructureModel */
export interface SigningStructureModel {
  /** Certificates Chain */
  certificates_chain?: CertificateInfoModel[] | null;
  /** Issuer */
  issuer?: SignersModel[] | null;
  /** Signature Timestamp Time */
  signature_timestamp_time?: string | null;
  /** Signing Time */
  signing_time?: string | null;
}

/** ValidationError */
export interface ValidationError {
  /** Location */
  loc: (string | number)[];
  /** Message */
  msg: string;
  /** Error Type */
  type: string;
}

/** VerificationModel */
export interface VerificationModel {
  /** Is Valid */
  is_valid: boolean;
  result?: SigningStructureModel | null;
}

export type QueryParamsType = Record<string | number, any>;
export type ResponseFormat = keyof Omit<Body, "body" | "bodyUsed">;

export interface FullRequestParams extends Omit<RequestInit, "body"> {
  /** set parameter to `true` for call `securityWorker` for this request */
  secure?: boolean;
  /** request path */
  path: string;
  /** content type of request body */
  type?: ContentType;
  /** query params */
  query?: QueryParamsType;
  /** format of response (i.e. response.json() -> format: "json") */
  format?: ResponseFormat;
  /** request body */
  body?: unknown;
  /** base url */
  baseUrl?: string;
  /** request cancellation token */
  cancelToken?: CancelToken;
}

export type RequestParams = Omit<
  FullRequestParams,
  "body" | "method" | "query" | "path"
>;

export interface ApiConfig<SecurityDataType = unknown> {
  baseUrl?: string;
  baseApiParams?: Omit<RequestParams, "baseUrl" | "cancelToken" | "signal">;
  securityWorker?: (
    securityData: SecurityDataType | null,
  ) => Promise<RequestParams | void> | RequestParams | void;
  customFetch?: typeof fetch;
}

export interface HttpResponse<D extends unknown, E extends unknown = unknown>
  extends Response {
  data: D;
  error: E;
}

type CancelToken = Symbol | string | number;

export enum ContentType {
  Json = "application/json",
  JsonApi = "application/vnd.api+json",
  FormData = "multipart/form-data",
  UrlEncoded = "application/x-www-form-urlencoded",
  Text = "text/plain",
}

export class HttpClient<SecurityDataType = unknown> {
  public baseUrl: string = "";
  private securityData: SecurityDataType | null = null;
  private securityWorker?: ApiConfig<SecurityDataType>["securityWorker"];
  private abortControllers = new Map<CancelToken, AbortController>();
  private customFetch = (...fetchParams: Parameters<typeof fetch>) =>
    fetch(...fetchParams);

  private baseApiParams: RequestParams = {
    credentials: "same-origin",
    headers: {},
    redirect: "follow",
    referrerPolicy: "no-referrer",
  };

  constructor(apiConfig: ApiConfig<SecurityDataType> = {}) {
    Object.assign(this, apiConfig);
  }

  public setSecurityData = (data: SecurityDataType | null) => {
    this.securityData = data;
  };

  protected encodeQueryParam(key: string, value: any) {
    const encodedKey = encodeURIComponent(key);
    return `${encodedKey}=${encodeURIComponent(typeof value === "number" ? value : `${value}`)}`;
  }

  protected addQueryParam(query: QueryParamsType, key: string) {
    return this.encodeQueryParam(key, query[key]);
  }

  protected addArrayQueryParam(query: QueryParamsType, key: string) {
    const value = query[key];
    return value.map((v: any) => this.encodeQueryParam(key, v)).join("&");
  }

  protected toQueryString(rawQuery?: QueryParamsType): string {
    const query = rawQuery || {};
    const keys = Object.keys(query).filter(
      (key) => "undefined" !== typeof query[key],
    );
    return keys
      .map((key) =>
        Array.isArray(query[key])
          ? this.addArrayQueryParam(query, key)
          : this.addQueryParam(query, key),
      )
      .join("&");
  }

  protected addQueryParams(rawQuery?: QueryParamsType): string {
    const queryString = this.toQueryString(rawQuery);
    return queryString ? `?${queryString}` : "";
  }

  private contentFormatters: Record<ContentType, (input: any) => any> = {
    [ContentType.Json]: (input: any) =>
      input !== null && (typeof input === "object" || typeof input === "string")
        ? JSON.stringify(input)
        : input,
    [ContentType.JsonApi]: (input: any) =>
      input !== null && (typeof input === "object" || typeof input === "string")
        ? JSON.stringify(input)
        : input,
    [ContentType.Text]: (input: any) =>
      input !== null && typeof input !== "string"
        ? JSON.stringify(input)
        : input,
    [ContentType.FormData]: (input: any) => {
      if (input instanceof FormData) {
        return input;
      }

      return Object.keys(input || {}).reduce((formData, key) => {
        const property = input[key];
        formData.append(
          key,
          property instanceof Blob
            ? property
            : typeof property === "object" && property !== null
              ? JSON.stringify(property)
              : `${property}`,
        );
        return formData;
      }, new FormData());
    },
    [ContentType.UrlEncoded]: (input: any) => this.toQueryString(input),
  };

  protected mergeRequestParams(
    params1: RequestParams,
    params2?: RequestParams,
  ): RequestParams {
    return {
      ...this.baseApiParams,
      ...params1,
      ...(params2 || {}),
      headers: {
        ...(this.baseApiParams.headers || {}),
        ...(params1.headers || {}),
        ...((params2 && params2.headers) || {}),
      },
    };
  }

  protected createAbortSignal = (
    cancelToken: CancelToken,
  ): AbortSignal | undefined => {
    if (this.abortControllers.has(cancelToken)) {
      const abortController = this.abortControllers.get(cancelToken);
      if (abortController) {
        return abortController.signal;
      }
      return void 0;
    }

    const abortController = new AbortController();
    this.abortControllers.set(cancelToken, abortController);
    return abortController.signal;
  };

  public abortRequest = (cancelToken: CancelToken) => {
    const abortController = this.abortControllers.get(cancelToken);

    if (abortController) {
      abortController.abort();
      this.abortControllers.delete(cancelToken);
    }
  };

  public request = async <T = any, E = any>({
    body,
    secure,
    path,
    type,
    query,
    format,
    baseUrl,
    cancelToken,
    ...params
  }: FullRequestParams): Promise<HttpResponse<T, E>> => {
    const secureParams =
      ((typeof secure === "boolean" ? secure : this.baseApiParams.secure) &&
        this.securityWorker &&
        (await this.securityWorker(this.securityData))) ||
      {};
    const requestParams = this.mergeRequestParams(params, secureParams);
    const queryString = query && this.toQueryString(query);
    const payloadFormatter = this.contentFormatters[type || ContentType.Json];
    const responseFormat = format || requestParams.format;

    return this.customFetch(
      `${baseUrl || this.baseUrl || ""}${path}${queryString ? `?${queryString}` : ""}`,
      {
        ...requestParams,
        headers: {
          ...(requestParams.headers || {}),
          ...(type && type !== ContentType.FormData
            ? { "Content-Type": type }
            : {}),
        },
        signal:
          (cancelToken
            ? this.createAbortSignal(cancelToken)
            : requestParams.signal) || null,
        body:
          typeof body === "undefined" || body === null
            ? null
            : payloadFormatter(body),
      },
    ).then(async (response) => {
      const r = response as HttpResponse<T, E>;
      r.data = null as unknown as T;
      r.error = null as unknown as E;

      const responseToParse = responseFormat ? response.clone() : response;
      const data = !responseFormat
        ? r
        : await responseToParse[responseFormat]()
            .then((data) => {
              if (r.ok) {
                r.data = data;
              } else {
                r.error = data;
              }
              return r;
            })
            .catch((e) => {
              r.error = e;
              return r;
            });

      if (cancelToken) {
        this.abortControllers.delete(cancelToken);
      }

      if (!response.ok) throw data;
      return data;
    });
  };
}

/**
 * @title Модуль подписания
 * @version 1.0.0
 */
export class Api<
  SecurityDataType extends unknown,
> extends HttpClient<SecurityDataType> {
  api = {
    /**
     * No description
     *
     * @name CreateHashApiV1CreateHashPost
     * @summary Создание хеша документа
     * @request POST:/api/v1/create_hash
     */
    createHashApiV1CreateHashPost: (
      data: BodyCreateHashApiV1CreateHashPost,
      params: RequestParams = {},
    ) =>
      this.request<any, HTTPValidationError>({
        path: `/api/v1/create_hash`,
        method: "POST",
        body: data,
        type: ContentType.FormData,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @name VerifySignatureApiV1VerifySignaturePost
     * @summary Проверка подписи
     * @request POST:/api/v1/verify_signature
     */
    verifySignatureApiV1VerifySignaturePost: (
      data: BodyVerifySignatureApiV1VerifySignaturePost,
      params: RequestParams = {},
    ) =>
      this.request<
        ResponseDataModelVerificationModel,
        ResponseDataModel | ResponseDataModelVerificationModel
      >({
        path: `/api/v1/verify_signature`,
        method: "POST",
        body: data,
        type: ContentType.FormData,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @name GetRootCertificatesApiV1GetRootCertificatesStoreNameGet
     * @summary Сертифкаты
     * @request GET:/api/v1/get_root_certificates/{store_name}
     */
    getRootCertificatesApiV1GetRootCertificatesStoreNameGet: (
      storeName: StoreNamePathModel,
      params: RequestParams = {},
    ) =>
      this.request<
        ResponseDataModelListCertificateInfoModel,
        ResponseDataModel | ResponseDataModelNoneType
      >({
        path: `/api/v1/get_root_certificates/${storeName}`,
        method: "GET",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @name SetPersonalCertificatesApiV1SetCertificateStoreNamePost
     * @summary Загрузить сертифкат
     * @request POST:/api/v1/set_certificate/{store_name}
     */
    setPersonalCertificatesApiV1SetCertificateStoreNamePost: (
      storeName: StoreNamePathModel,
      data: BodySetPersonalCertificatesApiV1SetCertificateStoreNamePost,
      params: RequestParams = {},
    ) =>
      this.request<
        ResponseDataModelCertificateInfoModel,
        ResponseDataModelNoneType | ResponseDataModel
      >({
        path: `/api/v1/set_certificate/${storeName}`,
        method: "POST",
        body: data,
        type: ContentType.FormData,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @name RemoveCertificateApiV1RemoveCertificatePost
     * @summary Удалить сертифкат
     * @request POST:/api/v1/remove_certificate
     */
    removeCertificateApiV1RemoveCertificatePost: (
      data: RemoveCertificateBodyModel,
      params: RequestParams = {},
    ) =>
      this.request<
        ResponseDataModelCertificateInfoModel,
        ResponseDataModel | ResponseDataModelNoneType
      >({
        path: `/api/v1/remove_certificate`,
        method: "POST",
        body: data,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),
  };
}
