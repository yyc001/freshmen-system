import { createFileRoute } from '@tanstack/react-router'
import PageContent from '../../components/PageContent'
import { Col, Row } from 'antd';

export const Route = createFileRoute('/help/examples')({
  component: () => {
    return (
        <>
        <PageContent>
        <h1>获奖证书样例 - 泰山学堂新生报名系统</h1>
        <h2>下面是部分获奖证书的样例</h2>
        <Row gutter={[16, 24]}>
            <Col className="gutter-row" span={8}>
                <div>
                <label>全国中学生物理竞赛决赛</label>
                <img src={"/awards/物理国赛.png"} style={{maxWidth: '100%'}} alt='物理国赛.png'/>
                </div>
            </Col>
            <Col className="gutter-row" span={8}>
                <div>
                <label>全国中学生物理竞赛复赛（省级赛区）[一等奖]</label>
                <img src={"/awards/物理省一.png"} style={{maxWidth: '100%'}} alt='物理省一.png'/>
                </div>
            </Col>
            <Col className="gutter-row" span={8}>
                <div>
                <label>全国中学生物理竞赛复赛（省级赛区）[二等奖]</label>
                <img src={"/awards/物理省二.png"} style={{maxWidth: '100%'}} alt='物理省二.png'/>
                </div>
            </Col>
            <Col className="gutter-row" span={8}>
                <div>
                <label>全国中学生物理竞赛复赛（省级赛区）[三等奖]</label>
                <img src={"/awards/物理省三.png"} style={{maxWidth: '100%'}} alt='物理省三.png'/>
                </div>
            </Col>
        </Row>
        </PageContent> 
      </>
    )
  },
})