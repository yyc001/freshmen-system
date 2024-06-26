/* prettier-ignore-start */

/* eslint-disable */

// @ts-nocheck

// noinspection JSUnusedGlobalSymbols

// This file is auto-generated by TanStack Router

import { createFileRoute } from '@tanstack/react-router'

// Import Routes

import { Route as rootRoute } from './routes/__root'
import { Route as RegServiceHallImport } from './routes/reg/service-hall'
import { Route as RegReadySubmitImport } from './routes/reg/ready-submit'
import { Route as RegContactDetailsImport } from './routes/reg/contact-details'
import { Route as RegBasicInfoImport } from './routes/reg/basic-info'
import { Route as RegAttachmentsImport } from './routes/reg/attachments'
import { Route as ManageSubmissionsImport } from './routes/manage/submissions'
import { Route as ManageViewUidImport } from './routes/manage/view.$uid'

// Create Virtual Routes

const HelpLazyImport = createFileRoute('/help')()
const IndexLazyImport = createFileRoute('/')()
const ManageControlPanelLazyImport = createFileRoute('/manage/control-panel')()

// Create/Update Routes

const HelpLazyRoute = HelpLazyImport.update({
  path: '/help',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/help.lazy').then((d) => d.Route))

const IndexLazyRoute = IndexLazyImport.update({
  path: '/',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/index.lazy').then((d) => d.Route))

const ManageControlPanelLazyRoute = ManageControlPanelLazyImport.update({
  path: '/manage/control-panel',
  getParentRoute: () => rootRoute,
} as any).lazy(() =>
  import('./routes/manage/control-panel.lazy').then((d) => d.Route),
)

const RegServiceHallRoute = RegServiceHallImport.update({
  path: '/reg/service-hall',
  getParentRoute: () => rootRoute,
} as any)

const RegReadySubmitRoute = RegReadySubmitImport.update({
  path: '/reg/ready-submit',
  getParentRoute: () => rootRoute,
} as any)

const RegContactDetailsRoute = RegContactDetailsImport.update({
  path: '/reg/contact-details',
  getParentRoute: () => rootRoute,
} as any)

const RegBasicInfoRoute = RegBasicInfoImport.update({
  path: '/reg/basic-info',
  getParentRoute: () => rootRoute,
} as any)

const RegAttachmentsRoute = RegAttachmentsImport.update({
  path: '/reg/attachments',
  getParentRoute: () => rootRoute,
} as any)

const ManageSubmissionsRoute = ManageSubmissionsImport.update({
  path: '/manage/submissions',
  getParentRoute: () => rootRoute,
} as any)

const ManageViewUidRoute = ManageViewUidImport.update({
  path: '/manage/view/$uid',
  getParentRoute: () => rootRoute,
} as any)

// Populate the FileRoutesByPath interface

declare module '@tanstack/react-router' {
  interface FileRoutesByPath {
    '/': {
      preLoaderRoute: typeof IndexLazyImport
      parentRoute: typeof rootRoute
    }
    '/help': {
      preLoaderRoute: typeof HelpLazyImport
      parentRoute: typeof rootRoute
    }
    '/manage/submissions': {
      preLoaderRoute: typeof ManageSubmissionsImport
      parentRoute: typeof rootRoute
    }
    '/reg/attachments': {
      preLoaderRoute: typeof RegAttachmentsImport
      parentRoute: typeof rootRoute
    }
    '/reg/basic-info': {
      preLoaderRoute: typeof RegBasicInfoImport
      parentRoute: typeof rootRoute
    }
    '/reg/contact-details': {
      preLoaderRoute: typeof RegContactDetailsImport
      parentRoute: typeof rootRoute
    }
    '/reg/ready-submit': {
      preLoaderRoute: typeof RegReadySubmitImport
      parentRoute: typeof rootRoute
    }
    '/reg/service-hall': {
      preLoaderRoute: typeof RegServiceHallImport
      parentRoute: typeof rootRoute
    }
    '/manage/control-panel': {
      preLoaderRoute: typeof ManageControlPanelLazyImport
      parentRoute: typeof rootRoute
    }
    '/manage/view/$uid': {
      preLoaderRoute: typeof ManageViewUidImport
      parentRoute: typeof rootRoute
    }
  }
}

// Create and export the route tree

export const routeTree = rootRoute.addChildren([
  IndexLazyRoute,
  HelpLazyRoute,
  ManageSubmissionsRoute,
  RegAttachmentsRoute,
  RegBasicInfoRoute,
  RegContactDetailsRoute,
  RegReadySubmitRoute,
  RegServiceHallRoute,
  ManageControlPanelLazyRoute,
  ManageViewUidRoute,
])

/* prettier-ignore-end */
